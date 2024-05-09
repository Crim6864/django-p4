# In your app's forms.py file
from django import forms
from .models import Profile, Gymnast


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "förnamn",
            "efternamn",
            "adress",
            "telefon",
        ]  # Add any additional fields you want to include in the form


class GymnastForm(forms.ModelForm):
    class Meta:
        model = Gymnast  # Use the correct model name here
        fields = [
            "förnamn",
            "efternamn",
            "personnummer",
            "grupp",
        ]  # Specify the fields you want to include in the form
