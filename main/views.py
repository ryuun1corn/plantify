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


def redirect_home(request):
    return redirect("home/")
