from django import forms
from .models import Gymnast

class GymnastForm(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = ['förnamn', 'efternamn', 'personnummer', 'grupp', 'parent1', 'parent2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grupp'].required = False
        self.fields['grupp'].widget = forms.HiddenInput()
        self.fields['parent1'].widget = forms.HiddenInput()
        self.fields['parent1'].required = False
        self.fields['parent2'].widget = forms.HiddenInput()
        self.fields['parent2'].required = False

    def clean_parent2(self):
        parent1 = self.cleaned_data.get('parent1')
        parent2 = self.cleaned_data.get('parent2')
        if parent1 and not parent1.is_superuser:
            raise forms.ValidationError("Only admins can edit parent2.")
        return parent2
