from django import forms
from django.core.exceptions import ValidationError
from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'email', 'phone_number', 'address', 'group', 'grade',
            'parent_name', 'parent_phone', 'parent_email', 'profile_photo'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter last name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'gender': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter phone number'}),
            'group': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'grade': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'address': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'rows': 3, 'placeholder': 'Enter full address'}),
            'parent_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter parent/guardian name'}),
            'parent_phone': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter parent/guardian phone'}),
            'parent_email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'placeholder': 'Enter parent/guardian email'}),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_group(self):
        """Guruhi tanlanganida, undagi talabalar soni max_students dan oshmasligini tekshiradi."""
        group = self.cleaned_data.get('group')

        if group:
            current_students_count = group.students.count()  # Guruhdagi hozirgi talabalar soni
            max_students = group.max_students  # Guruhning maksimal talaba soni

            if max_students is not None and current_students_count >= max_students:
                raise ValidationError(f"{group.name} guruhiga yangi talabalar qo‘shish mumkin emas (Maksimal: {max_students}).")

        return group
