"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import petstore


def index(request: HttpRequest) -> HttpResponse:  # TODO: pagination
    return render(request, "DEIPet/index.html", {"pets": petstore.get_pets()})


def create_pet(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hi")