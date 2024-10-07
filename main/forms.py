from django.forms import ModelForm
from django.utils.html import strip_tags

from main.models import TropicalPlant


class TropicalPlantEntryForm(ModelForm):
    class Meta:
        model = TropicalPlant
        fields = ["name", "price", "description", "weight"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
