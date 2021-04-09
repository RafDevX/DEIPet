"""URL configuration for the DEIPet application"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-pet", views.create_pet, name="create-pet"),
]
