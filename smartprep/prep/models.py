from django.db import models

# Create your models here.

class Uebung(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    titel = models.CharField(max_length=100)
    fach = models.TextField()
    thema = models.TextField(max_length=100)
    frage = models.TextField(max_length=200)
    antwort = models.TextField()
    slug = models.SlugField(unique=True)


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField(max_length=100)
    vorname = models.TextField(max_length=100)
    strasse = models.TextField(max_length=100)
    stadt = models.TextField(max_length=100)
    geburtstag = models.DateField()
    slug = models.SlugField(unique=True)


    