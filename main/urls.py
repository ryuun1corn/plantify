from django.urls import path

from main.views import (
    add_tropical_plant,
    add_tropical_plant_ajax,
    delete_tropical_plant,
    edit_tropical_plant,
    get_tropical_plant_json,
    get_tropical_plant_xml,
    get_tropical_plants_json,
    get_tropical_plants_xml,
    login_user,
    logout_user,
    redirect_home,
    register,
    show_main,
)

app_name = "main"


urlpatterns = [
    path("home/", show_main, name="show_main"),
    path("", redirect_home, name="redirect_home"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("add-tropical-plant/", add_tropical_plant, name="add_tropical_plant"),
    path(
        "edit-tropical-plant/<uuid:id>", edit_tropical_plant, name="edit_tropical_plant"
    ),
    path(
        "delete-tropical-plant/<uuid:id>",
        delete_tropical_plant,
        name="delete_tropical_plant",
    ),  # sesuaikan dengan nama fungsi yang dibuat
    path(
        "tropical-plant-xml/", get_tropical_plants_xml, name="get_tropical_plants_xml"
    ),
    path(
        "tropical-plant-json/",
        get_tropical_plants_json,
        name="get_tropical_plants_json",
    ),
    path(
        "tropical-plant-xml/<str:id>/",
        get_tropical_plant_xml,
        name="get_tropical_plant_xml",
    ),
    path(
        "tropical-plant-json/<str:id>/",
        get_tropical_plant_json,
        name="get_tropical_plant_json",
    ),
    path(
        "create-ajax/",
        add_tropical_plant_ajax,
        name="create_ajax",
    ),
]
