from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home ), #our-domain.com/prep
    path('fach/', views.fach ) #our-domain.com/prep
]