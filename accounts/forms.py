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
    """
    Form for updating the user's profile.
    """

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="New Password"
    )
    repeat_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="Repeat Password"
    )

    class Meta:
        model = UserProfile
        fields = ('bio', 'birth_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
            })

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        repeat_password = cleaned_data.get("repeat_password")

        if new_password and new_password != repeat_password:
            self.add_error("repeat_password", "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user_profile = super().save(commit=False)

        # Update password if provided
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            user_profile.user.set_password(new_password)
            user_profile.user.save()

        if commit:
            user_profile.save()
        return user_profile
