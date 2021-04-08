"""View controllers for the DEIPet application"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Woo!")