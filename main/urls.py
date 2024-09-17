from django.urls import path

from main.views import add_tropical_plant, redirect_home, show_main

app_name = "main"

urlpatterns = [
    path("home/", show_main, name="show_main"),
    path("", redirect_home, name="redirect_home"),
    path("add-tropical-plant", add_tropical_plant, name="add_tropical_plant"),
]
