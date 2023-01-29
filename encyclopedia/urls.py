from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>/", views.entry, name="entry"), 
    path("search", views.search, name="search"), 
    path("new", views.new, name="new"), 
    path("edit", views.edit, name="edit"),
    path("edit_save", views.edit_save, name="edit_save"),
    path("rand", views.rand, name="rand")
]

