"""URL configuration for the DEIPet application"""

from django.shortcuts import redirect
from django.urls import path

from . import views

app_name = "DEIPet"
urlpatterns = [
    path("", lambda r: redirect("DEIPet:list-pets-start"), name="index"),
    path("pets", views.list_pets, name="list-pets-start"),
    path("pets/page-<int:page>-size-<int:pg_size>", views.list_pets, name="list-pets"),
    path("pet/<int:id>", views.pet_info, name="pet-info"),
    path("pet/<int:id>/<str:status>", views.pet_info, name="pet-info-postaction"),
    path("create-pet", views.create_pet, name="create-pet"),
]

# TODO: handler404
# TODO: page size should go to page 1 or stay?
# TODO: required/validation in create_pet.html
# TODO: two images required
# TODO: "clique num deles para ver detalhes"?