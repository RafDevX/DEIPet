"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import petstore


def list_pets(request: HttpRequest) -> HttpResponse:
    # TODO: pagination
    # GET params examples:
    #   - page=1
    #   - sortBy=name-asc, sortBy=id, sortBy=name-bad
    page = 1
    possible_sorts, possible_dirs = ("id", "name"), ("asc", "dsc")
    sort_by, sort_dir = possible_sorts[0], possible_dirs[0]
    if "sortBy" in request.GET:
        sort_inp = request.GET["sortBy"]

        if sort_inp in possible_sorts:
            sort_by = sort_inp
        elif request.GET["sortBy"][:-4] in possible_sorts:
            sort_by = sort_inp[:-4]

        if request.GET["sortBy"][-3:] in possible_dirs:
            sort_dir = sort_inp[-3:]

    normalized_query = "?page=" + str(page) + "&sortBy=" + sort_by + "-" + sort_dir

    return render(
        request,
        "DEIPet/index.html",
        {
            "pets": sorted(
                petstore.get_pets(), key=lambda k: k[sort_by], reverse=sort_dir == "dsc"
            ),
            "sort_by": sort_by,
            "sort_dir": sort_dir,
        },
    )


def create_pet(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hi")