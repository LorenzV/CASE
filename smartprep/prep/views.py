from django.core.files.base import equals_lf
from django.shortcuts import render, redirect

from prep.forms import AntwortForm

from .models import Uebung
from .models import Thema

from django.contrib.auth.models import User


# Create your views here.


def home(request):

    return render(request, 'prep/home.html', {

})



def math(request):
    uebung = Uebung.objects.all()

    if request.user.is_authenticated:
    # Do something for authenticated users.

        return render(request, 'prep/math.html', {
        'uebung':uebung
    })
    else:
    # Do something for anonymous users.
        return render(request, 'registration/notloggedin.html', {
    })



def theorie(request):
    thema = Thema.objects.all()
    
    if request.user.is_authenticated:
    # Do something for authenticated users.

        return render(request, 'prep/theorie.html', {
            'thema':thema
        })
    else:
    # Do something for anonymous users.
        return render(request, 'registration/notloggedin.html', {
    })

def uebung(request, uebung_slug):
    try:
        selected_uebung = Uebung.objects.get(slug=uebung_slug)
        if request.method =="GET":
            antwort_form = AntwortForm()
            return render(request,'prep/uebung.html', {
                    'uebung_found': True,
                    'uebung_titel': selected_uebung.titel,
                    'uebung_frage': selected_uebung.frage,
                    'uebung_antwort':selected_uebung.antwort,
                    'form': antwort_form,
            })
        else:
            antwort = request.POST.__getitem__('antwort')          
            if antwort == selected_uebung.antwort:
                antwort_form = AntwortForm(request.POST)               
                return redirect("/math")
            else:
                antwort_form = AntwortForm(request.GET)

        return render(request,'prep/uebung.html', {
                    'uebung_found': True,
                    'uebung_titel': selected_uebung.titel,
                    'uebung_frage': selected_uebung.frage,
                    'uebung_antwort':selected_uebung.antwort,
                    'form': antwort_form,
            })
            
    except Exception as exc:
        return render(request,'prep/uebung.html',{
            'uebung:Found': False
        })

def thema(request, thema_slug):
    try:
        selected_thema=Thema.objects.get(slug=thema_slug)

        return render(request,'prep/thema.html',{
            'thema_found':True,
            'thema_name':selected_thema.name,
            'thema_inhalt':selected_thema.inhalt
        })
    except Exception as exc:
        return render(request,'prep/theorie.html',{
            'theorie_found':False
        })





