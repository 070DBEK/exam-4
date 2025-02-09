from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from students.models import Student
from students.forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Students"
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/detail.html"
    context_object_name = "student"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/form.html"
    success_url = reverse_lazy("students:list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/form.html"
    success_url = reverse_lazy("students:list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("students:list")
