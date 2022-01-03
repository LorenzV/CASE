from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/home')),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home' ), #our-domain.com/home
    path('math/', views.math, name='math'), #our-domain.com/math
    path('theorie/', views.theorie, name='theorie'), #our-domain.com/theorie
    
    path('math/<slug:uebung_slug>/', views.uebung, name='uebung'), #our-domain.com/"username"/uebungxxx
    path('theorie/<slug:thema_slug>/', views.thema, name='thema'), #our-domain.com/"username"/uebungxxx

    ]