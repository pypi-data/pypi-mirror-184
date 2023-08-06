from typing import Optional, cast

import requests

from .types import SearchEntriesCollection, FuelTypeEnum, SortMethod

TIMEOUT = 3
BASE_URI = "https://app.petrolprices.com"


class PetrolPricesException(RuntimeError):
    """Unknown error"""


class UnauthorizedException(PetrolPricesException):
    """Unauthorized"""


class NotFoundException(PetrolPricesException):
    """Not Found"""


class PetrolPrices:
    def __init__(self, api_token: str, base_uri: str = BASE_URI) -> None:
        self.api_token: str = api_token
        self.base_uri: str = base_uri
        self.headers: dict = {
            "Authorization": "Bearer {0}".format(self.api_token),
            "Cookie": "auth={0}".format(self.api_token),
        }

    def search(
        self,
        latitude: float,
        longitude: float,
        fuel_type: FuelTypeEnum = FuelTypeEnum.Unleaded,
        sort_method: SortMethod = SortMethod.Cheapest,
        max_distance: int = 5,
    ) -> SearchEntriesCollection:
        response = self.get(
            "/geojson/{3}/0/0/0/{2}/{4}?lat={0}&longitude={1}".format(
                latitude, longitude, sort_method.value, fuel_type.value, max_distance
            )
        )

        return cast(
            SearchEntriesCollection,
            {"data": response.get("data").get("features") or []},
        )

    def get(self, url: str):
        return self.__request("GET", url)

    def post(self, url: str, data: Optional[dict] = None):
        if data is None:
            data = {}
        return self.__request("POST", url, data)

    def __request(self, method: str, url: str, params: Optional[dict] = None):
        if params is None:
            params = {}

        if method == "GET":
            response = requests.get(
                self.base_uri + url, params=params, headers=self.headers
            )
        elif method == "POST":
            response = requests.post(
                self.base_uri + url, json=params, headers=self.headers
            )
        else:
            raise RuntimeError("Invalid request method provided")

        if response.status_code == 401:
            raise UnauthorizedException(response.json().get("error"))
        if response.status_code == 404:
            raise NotFoundException(response.json().get("error"))
        if response.status_code >= 400:
            raise PetrolPricesException(response.json().get("error") or "Unknown error")
        return response.json()
