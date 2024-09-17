from django.forms import ModelForm

from main.models import TropicalPlant


class TropicalPlantEntryForm(ModelForm):
    class Meta:
        model = TropicalPlant
        fields = ["name", "price", "description", "weight"]
