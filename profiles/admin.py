from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "förnamn", "efternamn", "adress", "telefon")

# Correct placement of admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile, ProfileAdmin)
