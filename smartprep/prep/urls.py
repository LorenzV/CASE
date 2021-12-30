from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home ), #our-domain.com/prep
    path('math/', views.math ), #our-domain.com/prep
    path('uebung/', views.uebung ) #our-domain.com/prep
]