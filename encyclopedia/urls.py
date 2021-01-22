from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/", views.random_page, name="randomPage"),
    path("create", views.create, name="create")
]
