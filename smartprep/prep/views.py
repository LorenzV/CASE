from django.shortcuts import render

from prep.models import Uebung


# Create your views here.


def home(request):
        
    return render(request, 'prep/home.html', {
    })

def fach(request):
    
    
    return render(request, 'prep/fach.html', {
    })



