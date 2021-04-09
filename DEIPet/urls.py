"""URL configuration for the DEIPet application"""

from django.urls import path

from . import views

app_name = "DEIPet"
urlpatterns = [
    path("", views.index, name="index"),
    path("create-pet", views.create_pet, name="create-pet"),
]
