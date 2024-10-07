import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main.forms import TropicalPlantEntryForm
from main.models import TropicalPlant


# Create your views here.
@login_required(login_url="/login")
def show_main(request):
    tropical_plant_entries = TropicalPlant.objects.filter(user=request.user)
    context = {
        "app_name": "Plantify",
        "name": request.user.username,
        "class": "PBP-D",
        "npm": "2306215160",
        "tropical_plants": tropical_plant_entries,
        "last_login": request.COOKIES["last_login"],
    }

    return render(request, "main.html", context)


def add_tropical_plant(request):
    form = TropicalPlantEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        tropical_plant_entry = form.save(commit=False)
        tropical_plant_entry.user = request.user
        tropical_plant_entry.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "add_tropical_plant.html", context)


def get_tropical_plants_xml(request):
    plants = TropicalPlant.objects.all()
    return HttpResponse(
        serializers.serialize("xml", plants), content_type="application/xml"
    )


def get_tropical_plants_json(request):
    plants = TropicalPlant.objects.all()
    return HttpResponse(
        serializers.serialize("json", plants), content_type="application/json"
    )


def get_tropical_plant_xml(request, id):
    plant = TropicalPlant.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", plant), content_type="application/xml"
    )


def get_tropical_plant_json(request, id):
    plant = TropicalPlant.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", plant), content_type="application/json"
    )


def redirect_home(request):
    return redirect("home/")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has successfully been created!")
            return redirect("main:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie(
                "last_login",
                str(datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M %p")),
            )
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response


def edit_tropical_plant(request, id):
    # Get tropical plant berdasarkan ID
    plant = TropicalPlant.objects.get(pk=id)

    # Set Tropical Plant sebagai instance dari form
    form = TropicalPlantEntryForm(request.POST or None, instance=plant)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse("main:show_main"))

    context = {"form": form}
    return render(request, "edit_tropical_plant.html", context)


def delete_tropical_plant(request, id):
    # Get tropical plant berdasarkan ID
    plant = TropicalPlant.objects.get(pk=id)
    # Hapus plant
    plant.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse("main:show_main"))


@csrf_exempt
@require_POST
def add_tropical_plant_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    weight = request.POST.get("weight")

    new_tropical_plant = TropicalPlant(
        name=name, price=price, description=description, weight=weight
    )
    new_tropical_plant.save()

    return HttpResponse(b"Created", status=201)
