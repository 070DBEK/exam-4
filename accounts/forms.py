from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number')  # username saqlab qolindi

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
            })


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        }),
        label="Email"
    )

    def clean_username(self):
        email = self.cleaned_data.get("email")
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=email)
            return user.username  # Django autentifikatsiya username orqali ishlaydi
        except UserModel.DoesNotExist:
            raise ValidationError("Email not found. Please check and try again.")


class UserProfileForm(forms.ModelForm):
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

        # Parolni yangilash
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            user_profile.user.set_password(new_password)
            user_profile.user.save()

        if commit:
            user_profile.save()
        return user_profile
