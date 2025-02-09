from django import forms
from django.core.exceptions import ValidationError
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'grade_level', 'class_teacher', 'schedule', 'academic_year', 'max_students',
                  'description', 'subjects', 'students']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Enter group name'}),
            'grade_level': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'class_teacher': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'schedule': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'academic_year': forms.TextInput(
                attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'e.g., 2023-2024'}),
            'max_students': forms.NumberInput(
                attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Enter max students'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'rows': 4,
                                                 'placeholder': 'Enter group description'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': 'space-y-2'}),
            'students': forms.SelectMultiple(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        }

    def clean_max_students(self):
        """Validates that the number of selected students does not exceed max_students."""
        max_students = self.cleaned_data.get('max_students')
        students = self.cleaned_data.get('students')

        if max_students is not None and students is not None:
            if len(students) > max_students:
                raise ValidationError(f"Maximum students allowed: {max_students}. You selected {len(students)}.")

        return max_students
