from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User



# Create your models here.

class Thema(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    slug = models.SlugField(unique=True)
    name = models.TextField(max_length=100)
    inhalt = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Uebung(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    slug = models.SlugField(unique=True)
    titel = models.CharField(max_length=100)
    fach = models.TextField()
    thema = models.ForeignKey(Thema, on_delete=models.SET_NULL, null=True)
    frage = models.TextField(max_length=200)
    antwort = models.TextField() 
    username = models.ManyToManyField(User, blank=True, null=True)
    
    def __str__(self):
        return f'{self.titel}'


