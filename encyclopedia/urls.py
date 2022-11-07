from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.new_page, name="newpage"),
    path("wiki/<str:title>/editpage/", views.edit_page, name="editpage"),
    path("wiki/<str:title>/update/", views.update_page, name="update"),
    path("random/", views.random_page, name="random"),
]
