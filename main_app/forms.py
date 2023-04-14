from django.forms import ModelForm 
from .models import Sighting, Food


class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = ['location', 'date', 'description']

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

