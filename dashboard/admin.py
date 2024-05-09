from django.contrib import admin
from .models import Profile, Gymnast


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "förnamn", "efternamn", "adress", "telefon")

class GymnastAdmin(admin.ModelAdmin):
    list_display = ("pk", "förnamn", "efternamn", "grupp")

# Correct placement of admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Gymnast, GymnastAdmin)
