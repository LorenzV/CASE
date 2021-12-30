from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home' ), #our-domain.com/prep
    path('math/', views.math, name='math'), #our-domain.com/prep
    path('math/<slug:uebung_slug>/', views.uebung, name='uebung') #our-domain.com/"username"/uebungxxx
    ]