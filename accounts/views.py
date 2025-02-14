from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, TemplateView, View
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from subjects.models import Subject
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['total_teachers'] = Teacher.objects.count()
        context['total_groups'] = Group.objects.count()
        context['total_subjects'] = Subject.objects.count()
        return context

# API JSON response uchun funksiya
def enrollment_data(request):
    """ Talabalar soni bo‘yicha oylar kesimidagi statistikani jo‘natadi """
    data = {
        "labels": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        "datasets": [
            {
                "label": "2024 Enrollments",
                "data": list(Student.objects.values_list('id', flat=True)),  # Bu joyni real ma'lumot bilan o'zgartiring
                "borderColor": "#2563eb",
                "backgroundColor": "rgba(37, 99, 235, 0.1)",
                "fill": True,
                "tension": 0.4
            }
        ]
    }
    return JsonResponse(data)


def subject_distribution(request):
    subjects = Subject.objects.annotate(student_count=Count('student'))

    data = {
        "labels": [subject.name for subject in subjects],
        "datasets": [{
            "data": [subject.student_count for subject in subjects],
            "backgroundColor": [
                '#2563eb', '#9333ea', '#06b6d4', '#10b981', '#f59e0b', '#ef4444'
            ]
        }]
    }

    return JsonResponse(data)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/sign-up.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



class UserLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)



class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'accounts/profile-update.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user_profile = form.save(commit=False)
        user = self.request.user
        new_password = form.cleaned_data.get("new_password")

        if new_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(self.request, user)

        user_profile.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Profile"
        return context



class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:logout_success')


class LogoutSuccessView(TemplateView):
    template_name = "accounts/logout.html"
