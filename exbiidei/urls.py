"""ExBIIDei project-wide URL Configuration"""

from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("", lambda r: redirect("deipet/"), name="index"),
    path("deipet/", include("DEIPet.urls")),
]