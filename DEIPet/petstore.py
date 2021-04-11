"""Consumer for the external Petstore API"""

import requests
from json import JSONDecodeError

from django.conf import settings

BASE_URL = settings.PETSTORE_BASE_URL
ENDPOINTS = {k: BASE_URL + v for (k, v) in settings.PETSTORE_ENDPOINTS.items()}
ACCESS_TOKEN = settings.PETSTORE_ACCESS_TOKEN


def get_pets(limit: int = 30, offset: int = 0) -> list[dict]:
    """Fetch a subset of the pets in the Petstore."""

    r = requests.get(
        ENDPOINTS["get_pets"],
        params={
            "limit": limit,
            "offset": offset,
        },
    )
    if r.ok:
        try:
            return r.json()
        except JSONDecodeError:
            pass
    raise PetstoreError


def get_pets_page(page: int, page_size: int, one_more: bool = False) -> list[dict]:
    """Shorthand to fetch a specific page of pets from the Petstore."""

    return get_pets(page_size + int(one_more), page_size * (page - 1))


def create_pet(name: str, imageUrls: list[str]) -> dict:
    """Create a new pet in the Petstore."""

    r = requests.post(
        ENDPOINTS["create_pet"],
        json={"name": name, "imageUrls": imageUrls},
        headers={"Authorization": "Bearer " + ACCESS_TOKEN},
    )
    if r.ok:
        try:
            return r.json()
        except JSONDecodeError:
            pass
    raise PetstoreError


def delete_pet(id: int) -> bool:
    """Delete a pet from the Petstore."""

    r = requests.delete(
        ENDPOINTS["delete_pet"] % id,
        headers={"Authorization": "Bearer " + ACCESS_TOKEN},
    )
    if not r.ok:
        raise PetstoreError
    return True


def get_pet_info(id: int) -> dict:
    """Get information about a specific pet in the Petstore."""

    r = requests.get(ENDPOINTS["get_pet_info"] % id)
    if r.ok:
        try:
            return r.json()
        except JSONDecodeError:
            pass
    raise PetstoreError


class PetstoreError(Exception):
    """General exception for everything that goes wrong communicating with the Petstore."""

    pass