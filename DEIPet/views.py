"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import petstore

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:  # TODO: pagination
    return render(request, "DEIPet/index.html", {"pets": petstore.get_pets()})
