"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import petstore


def list_pets(request: HttpRequest, sort_by: str = "id") -> HttpResponse:
    # TODO: pagination
    return render(
        request,
        "DEIPet/index.html",
        {
            "pets": petstore.get_pets(),
            "sort_by": sort_by if sort_by in ("id", "name") else "id",
        },
    )


def create_pet(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hi")