from django.contrib import admin

from .models import Thema
from .models import Uebung

# Register your models here.

class ThemaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('id','name',)}

class UebungAdmin(admin.ModelAdmin):
    list_display = ('id', 'titel', 'fach', 'thema',)
    list_filter = ('fach', 'thema',)
    prepopulated_fields = {'slug':('titel','id', )}



admin.site.register(Uebung, UebungAdmin)
admin.site.register(Thema,ThemaAdmin)
    


