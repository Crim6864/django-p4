from django.contrib import admin
from .models import Gymnast

class GymnastAdmin(admin.ModelAdmin):
    list_display = ("pk", "förnamn", "efternamn", "personnummer", "grupp", "parent1", "parent2")

admin.site.register(Gymnast, GymnastAdmin)
