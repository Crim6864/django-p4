from django import forms
from .models import Gymnast

class GymnastForm(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = [
            "förnamn",
            "efternamn",
            "personnummer",
            "grupp",
            "parent1",  # Include field for parent 1
            "parent2",  # Include field for parent 2
        ] 
