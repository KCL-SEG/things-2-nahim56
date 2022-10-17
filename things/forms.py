from things import models
from django import forms
from .models import Thing
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name","description","quantity"]


        quantity = forms.NumberInput()

        description=forms.CharField(widget = forms.Textarea)
   
    