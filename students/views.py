from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from students.forms import StudentForm
from django.db.models import Q
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = "students"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone_number__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Students"
        context["search_query"] = self.request.GET.get("q", "")
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/detail.html"
    context_object_name = "student"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Student,
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/form.html"
    success_url = reverse_lazy("students:list")


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/form.html"
    success_url = reverse_lazy("students:list")


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("students:list")
