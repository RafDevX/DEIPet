"""Project-wide settings"""

import os

DEBUG = True  # False
ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]

SECRET_KEY = "eZD1a/GdFH2gIaKnqeAXgBtZZrwVoqA84mtJ6ZdUaZvjjECb6rdWSNAWTx1sHAYK"

PETSTORE_BASE_URL = "https://example.com"
PETSTORE_ENDPOINTS = {
    "get_pets": "/pets",
    "create_pet": "/pets",
    "delete_pet": "/pets/%d",
    "get_pet_info": "/pets/%d",
}
PETSTORE_ACCESS_TOKEN = os.getenv(
    "PETSTORE_ACCESS_TOKEN",
    "***HIDDEN***",
)  # (the token would not be here in a real project, this is just to make testing easier for the jury)

INSTALLED_APPS = [
    "DEIPet",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "exbiidei.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

WSGI_APPLICATION = "exbiidei.wsgi.application"

TIME_ZONE = "UTC"
USE_TZ = True

STATIC_URL = "/static/"
