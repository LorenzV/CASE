from django.shortcuts import render


# Create your views here.


def prep(request):
    faecher =[
    {'title': 'Mathematik'},
    {'title': 'Deutsch'}
    ]
    return render(request, 'prep/base.html', {
        'faecher': faecher
    })

