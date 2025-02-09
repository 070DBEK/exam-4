from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from .models import UserProfile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form, email is required for authentication.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'phone_number')  # username majburiy emas, lekin qoldirildi

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True  # Email majburiy qilish
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
            })


class CustomAuthenticationForm(forms.Form):
    """
    Custom authentication form, allowing users to log in with email and password.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
            'placeholder': 'name@school.com',
        }),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
            'placeholder': 'Enter your password',
        }),
        label="Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)  # Django username sifatida emailni qabul qiladi
            if not user:
                raise ValidationError("Email yoki parol noto‘g‘ri!")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, required=False)
    email = forms.EmailField(disabled=True, required=False)
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-full px-3 py-2 border rounded-md"}),
        required=False,
        label="New Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-full px-3 py-2 border rounded-md"}),
        required=False,
        label="Confirm Password"
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'bio', 'birth_date', 'phone_number', 'new_password', 'confirm_password']
        widgets = {
            "bio": forms.Textarea(attrs={"class": "w-full px-3 py-2 border rounded-md"}),
            "birth_date": forms.DateInput(attrs={"type": "date", "class": "w-full px-3 py-2 border rounded-md"}),
            "phone_number": forms.TextInput(attrs={"class": "w-full px-3 py-2 border rounded-md"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data
