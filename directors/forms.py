from django import forms
from .models import Director

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'bio', 'birth', 'picture']
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}),
        }
