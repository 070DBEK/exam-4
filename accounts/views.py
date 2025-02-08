from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, TemplateView, View
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = reverse_lazy('accounts:login')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/sign-up.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        user_profile = form.save(commit=False)
        new_password = form.cleaned_data.get("new_password")

        if new_password:
            self.request.user.set_password(new_password)
            self.request.user.save()
            update_session_auth_hash(self.request, self.request.user)

        user_profile.save()
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:logout_success')


class LogoutSuccessView(TemplateView):
    template_name = "accounts/logout.html"
