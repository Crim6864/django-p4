from django import forms
from .models import Gymnast

class GymnastForm(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = ['förnamn', 'efternamn', 'personnummer', 'grupp', 'parent1', 'parent2']  # Include 'parent2' field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grupp'].required = False
        self.fields['grupp'].widget = forms.HiddenInput()
        self.fields['parent1'].widget = forms.HiddenInput()
        self.fields['parent1'].required = False
        self.fields['parent2'].widget = forms.HiddenInput()
        self.fields['parent2'].required = False

    def clean_parent2(self):
        user = self.instance.parent1
        if user and not user.is_superuser:
            raise forms.ValidationError("Only admins can edit parent2.")
        return self.cleaned_data['parent2']
