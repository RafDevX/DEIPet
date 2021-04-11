"""View controllers for the DEIPet application"""

from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
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
            "pg_size_opts": range(10, 60, 10),
        },
    )


def pet_info(request: HttpRequest, id: int, status: Optional[str] = None):
    """Show a page that displays a specific pet's details."""

    success_msg, error_msg, not_found = None, None, False

    if status == "added":
        success_msg = "Animal de estimação adicionado com sucesso!"
    elif status == "failed-to-delete":
        error_msg = "Não foi possível eliminar o animal de estimação. Por favor tente mais tarde."

    fallback_image = static("DEIPet/images/fallback.png")

    try:
        pet = petstore.get_pet_info(id)
        pet["imageUrls"] = aux.filter_url_list(pet["imageUrls"], fallback_image)
    except petstore.PetstoreError:
        error_msg = "Animal de estimação não encontrado."
        pet = {"id": -1, "name": "Não Encontrado", "imageUrls": []}
        not_found = True

    return render(
        request,
        "DEIPet/pet_info.html",
        {
            "success_msg": success_msg,
            "error_msg": error_msg,
            "not_found": not_found,
            "pet_id": pet["id"],
            "pet_name": pet["name"],
            "pet_image_urls": pet["imageUrls"],
            "pet_details": [("ID", pet["id"]), ("Nome", pet["name"])],
        },
    )


def create_pet(request: HttpRequest) -> HttpResponse:
    "Show a page with a form to create a new pet and handle responses to it."

    error_msg, pet_name, pet_image_urls = None, "", []

    if request.POST and "petName" in request.POST and "petImageUrls" in request.POST:
        pet_name = request.POST["petName"]
        pet_image_urls = request.POST["petImageUrls"].splitlines()
        if len(pet_image_urls) < 2:
            error_msg = "É obrigatório incluir pelo menos duas imagens!"
        else:
            try:
                new_pet = petstore.create_pet(pet_name, pet_image_urls)
                return redirect(
                    "DEIPet:pet-info-postaction", id=new_pet["id"], status="added"
                )
            except petstore.PetstoreError:
                error_msg = "Ocorreu um erro a criar o animal de estimação. Por favor tente novamente."

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


def delete_pet(request: HttpRequest, id: int) -> HttpResponse:
    """Handle delete requests and show confirmation."""

    try:
        petstore.delete_pet(id)
        return render(request, "DEIPet/delete_pet.html", {"pet_id": id})
    except petstore.PetstoreError:
        pass
    return redirect("DEIPet:pet-info-postaction", id=id, status="failed-to-delete")
