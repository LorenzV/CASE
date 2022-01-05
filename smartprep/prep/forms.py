from django import forms
from .models import Uebung
from django.core.exceptions import ValidationError

class AntwortForm(forms.ModelForm):
    
    class Meta:
        model = Uebung
        fields = ['antwort']
    

