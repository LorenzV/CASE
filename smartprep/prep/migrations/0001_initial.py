# Generated by Django 3.2.5 on 2021-12-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uebung',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('titel', models.CharField(max_length=100)),
                ('fach', models.TextField()),
                ('thema', models.TextField(max_length=100)),
                ('frage', models.TextField(max_length=200)),
                ('antwort', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(max_length=100)),
                ('vorname', models.TextField(max_length=100)),
                ('strasse', models.TextField(max_length=100)),
                ('stadt', models.TextField(max_length=100)),
                ('geburtstag', models.DateField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
