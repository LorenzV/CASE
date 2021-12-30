from django.contrib import admin

from .models import Uebung
from .models import User

# Register your models here.

admin.site.register(Uebung)
admin.site.register(User)
