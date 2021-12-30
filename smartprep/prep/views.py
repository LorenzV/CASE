from django.shortcuts import render

from .models import Uebung

# Create your views here.


def home(request):
        
    return render(request, 'prep/home.html', {
    })


def math(request):
    uebung = Uebung.objects.all()
    
    return render(request, 'prep/math.html', {
        'show_uebung': True,
        'uebung':uebung
    })

def uebung(request, uebung_slug):
    selected_uebung = Uebung.objects.get(slug=uebung_slug)
        
    return render(request,'prep/uebung.html',{
        'uebung_titel': selected_uebung.titel,
        'uebung_frage': selected_uebung.frage,
        'uebung_antwort': selected_uebung.antwort
    })





