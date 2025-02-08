from django import forms
from .models import Department
from directors.models import Director


class DepartmentForm(forms.ModelForm):
    head = forms.ModelChoiceField(
        queryset=Director.objects.all(),
        required=False,
        empty_label="Select head of department"
    )

    class Meta:
        model = Department
        fields = ['name', 'head', 'description', 'location', 'contact_email', 'contact_phone']
