from django.shortcuts import render


# Create your views here.


def home(request):
    faecher =[
    {'title': 'Mathematik'},
    {'title': 'Deutsch'}
    ]
    return render(request, 'prep/home.html', {
        'faecher': faecher
    })

