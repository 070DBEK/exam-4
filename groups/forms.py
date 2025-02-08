from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'grade_level', 'class_teacher', 'schedule', 'academic_year', 'max_students', 'description', 'subjects']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Enter group name'}),
            'grade_level': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'class_teacher': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'schedule': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'academic_year': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'e.g., 2023-2024'}),
            'max_students': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Enter max students'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'rows': 4, 'placeholder': 'Enter group description'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': 'space-y-2'}),
        }
