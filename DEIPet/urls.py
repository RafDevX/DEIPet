"""URL configuration for the DEIPet application"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
