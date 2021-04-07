"""Consumer for the external Petstore API"""

import requests
from json import JSONDecodeError

BASE_URL = "https://example.com"
ENDPOINTS = {
    "get_pets": "/pets",
}


def get_pets(limit=30, offset=0):
    r = requests.get(
        BASE_URL + ENDPOINTS.get_pets,
        params={
            "limit": limit,
            "offset": offset,
        },
    )
    if r.ok:
        try:
            return r.json()  # try with raise JSONDecodeError and ValueError!!
        except JSONDecodeError:
            pass
    raise PetstoreError


class PetstoreError(Exception):
    pass