# In your app's forms.py file
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "förnamn",
            "efternamn",
            "adress",
            "telefon",
        ]  # Add any additional fields you want to include in the form
