# gymnast/admin.py
from django.contrib import admin
from .models import Gymnast, GymnastGroup

class GymnastAdmin(admin.ModelAdmin):
    list_display = ("pk", "förnamn", "efternamn", "personnummer", "grupp", "parent1", "parent2")

admin.site.register(Gymnast, GymnastAdmin)
admin.site.register(GymnastGroup)

