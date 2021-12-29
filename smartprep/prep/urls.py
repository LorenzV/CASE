from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.prep ), #our-domain.com/prep

]