"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.templatetags.static import static

from . import petstore, aux


def list_pets(request: HttpRequest, page=1, pg_size=30) -> HttpResponse:
    """Show a page that displays a list of pets with pagination."""

    page = page if page >= 1 else 1
    pg_size = pg_size if 1 <= pg_size <= 50 else 30

    error, prev_page_exists, next_page_exists, pets = False, False, False, []

    # get an extra item to see if next page exists
    try:
        pets = petstore.get_pets_page(page, pg_size + 1)
        prev_page_exists = page > 1
        if len(pets) > pg_size:
            next_page_exists = True
            pets = pets[:-1]
    except petstore.PetstoreError:
        error = True

    # don't cut the page range at the beginning for a single number (1 ... 3 4)
    pg_range = range(page - 2 if page >= 6 else 1, page + 1)

    # try to stop xss
    fallback_image = static("DEIPet/images/fallback.png")
    for pet in pets:
        pet["imageUrls"] = aux.filter_url_list(pet["imageUrls"], fallback_image)

    return render(
        request,
        "DEIPet/list_pets.html",
        {
            "error": error,
            "pets": pets,
            "page": page,
            "pg_size": pg_size,
            "prev_page_exists": prev_page_exists,
            "next_page_exists": next_page_exists,
            "pg_range": pg_range,
        },
    )


def pet_info(request: HttpRequest, id: int):
    return HttpResponse("hello")


def create_pet(request: HttpRequest) -> HttpResponse:
    "Show a page with a form to create a new pet and handle responses to it."

    error_msg, pet_name, pet_image_urls = None, "", ["a", "b", "c"]

    return render(
        request,
        "DEIPet/create_pet.html",
        {
            "error_msg": error_msg,
            "pet_name": pet_name,
            "pet_image_urls": pet_image_urls,
            "newline": "\n",
        },
    )
