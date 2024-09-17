from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect, render

from main.forms import TropicalPlantEntryForm
from main.models import TropicalPlant


# Create your views here.
def show_main(request):
    tropical_plant_entries = TropicalPlant.objects.all()
    context = {
        "app_name": "Plantify Shop",
        "name": "Yudayana Arif Prasojo",
        "class": "PBP-D",
        "npm": "2306215160",
        "tropical_plants": tropical_plant_entries,
    }

    return render(request, "main.html", context)


def add_tropical_plant(request):
    form = TropicalPlantEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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
