"""Consumer for the external Petstore API"""

import requests
from json import JSONDecodeError

from django.conf import settings

BASE_URL = settings.PETSTORE_BASE_URL
ENDPOINTS = {k: BASE_URL + v for (k, v) in settings.PETSTORE_ENDPOINTS.items()}
ACCESS_TOKEN = settings.PETSTORE_ACCESS_TOKEN


def get_pets(limit: int = 30, offset: int = 0) -> list[dict]:
    r = requests.get(
        BASE_URL + ENDPOINTS["get_pets"],
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


def create_pet(name: str, imageUrls: list) -> dict:
    r = requests.post(
        BASE_URL + ENDPOINTS["create_pet"],
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
    r = requests.delete(
        BASE_URL + (ENDPOINTS["delete_pet"] % id),
        headers={"Authorization": "Bearer " + ACCESS_TOKEN},
    )
    if not r.ok:
        raise PetstoreError
    return True


def get_pet_info(id: int) -> dict:
    r = requests.get(BASE_URL + (ENDPOINTS["get_pet_info"] % id))
    if r.ok:
        try:
            return r.json()
        except JSONDecodeError:
            pass
    raise PetstoreError


class PetstoreError(Exception):
    pass