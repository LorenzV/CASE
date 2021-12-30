from django.shortcuts import render

from prep.models import Uebung


# Create your views here.


def home(request):
        
    return render(request, 'prep/home.html', {
    })


def math(request):
    uebung = [
        {
            'titel': 'Test',
            'id': 1,
            'fach': 'Mathematik'      
        },
        {
            'titel': 'Test 3',
            'id': 12,
            'fach': 'Mathematik'      
    }]
    
    
    return render(request, 'prep/math.html', {
        'show_uebung': True,
        'uebung':uebung
    })

def uebung(request):
    selected_uebung ={
            'titel': 'Übung 1',
            'frage':'Testfrage ist Testfrage...',
            'antwort':'isch richtig!',
            'fach': 'Mathematik'      
        }
    return render(request,'prep/uebung.html',{
        'uebung_titel': selected_uebung['titel'],
        'uebung_frage': selected_uebung['frage'],
        'uebung_antwort': selected_uebung['antwort']
    })



