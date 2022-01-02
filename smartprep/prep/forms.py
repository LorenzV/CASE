from django import forms
from .models import Uebung

class AntwortForm(forms.ModelForm):

    class Meta:
        model = Uebung
        fields = ['antwort']

