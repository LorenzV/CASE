from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [

    path('home/', views.home, name='home' ), #our-domain.com/home
    path('math/', views.math, name='math'), #our-domain.com/math
    path('theorie/', views.theorie, name='theorie'), #our-domain.com/theori
    
    
    path('math/<slug:uebung_slug>/', views.uebung, name='uebung'), # our-domain.com/meetups/<dynamic-path-segment>

    path('theorie/<slug:thema_slug>/', views.thema, name='thema'), 

    path('', RedirectView.as_view(url='home/')),

    ]