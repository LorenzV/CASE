# Generated by Django 3.2.5 on 2022-01-03 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thema',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.TextField(max_length=100)),
                ('inhalt', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Uebung',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('titel', models.CharField(max_length=100)),
                ('fach', models.TextField()),
                ('frage', models.TextField(max_length=200)),
                ('antwort', models.TextField()),
                ('thema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prep.thema')),
            ],
        ),
    ]
