"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import petstore


def list_pets(request: HttpRequest, page=1, pg_size=30) -> HttpResponse:
    """Show a page that displays a list of pets with pagination."""

    page = page if page >= 1 else 1
    pg_size = pg_size if 1 <= pg_size <= 50 else 30

    # get an extra item to see if next page exists
    pets = petstore.get_pets_page(page, pg_size + 1)
    prev_page_exists = page > 1
    next_page_exists = len(pets) > pg_size
    pets = pets[:-1]

    # don't cut the page range at the beginning for a single number
    pg_range = range(page - 2 if page >= 6 else 1, page + 1)

    return render(
        request,
        "DEIPet/index.html",
        {
            "pets": pets,
            "page": page,
            "pg_size": pg_size,
            "prev_page_exists": prev_page_exists,
            "next_page_exists": next_page_exists,
            "pg_range": pg_range,
        },
    )


def create_pet(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hi")