"""Project-wide settings"""

DEBUG = True  # False
ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]

SECRET_KEY = "eZD1a/GdFH2gIaKnqeAXgBtZZrwVoqA84mtJ6ZdUaZvjjECb6rdWSNAWTx1sHAYK"

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
