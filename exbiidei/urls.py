"""ExBIIDei project-wide URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path("deipet/", include("DEIPet.urls")),
]

# TODO: handler404, etc