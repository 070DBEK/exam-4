from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SignUpForm, LoginForm


class DashboardView(LoginRequiredMixin, View):
    login_url = 'login'  # Foydalanuvchi login bo‘lmasa, ushbu URL-ga yo‘naltiriladi

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')


class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm  # Email orqali login qilish uchun forma
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


class SignUpView(FormView):
    template_name = "sign-up.html"  # Signup sahifasi
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard")  # Muvaffaqiyatli ro‘yxatdan o‘tganda

    def form_valid(self, form):
        user = form.save()  # Yangi foydalanuvchini yaratish
        login(self.request, user)  # Yangi foydalanuvchini avtomatik login qilish
        return super().form_valid(form)
