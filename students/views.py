from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from students.models import Student
from students.forms import StudentForm

# Student List View
class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = "students"

# Student Detail View
class StudentDetailView(DetailView):
    model = Student
    template_name = "students/detail.html"
    context_object_name = "student"


# Student Create View
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/form.html"
    success_url = reverse_lazy("students:list")

# Student Update View
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/form.html"
    success_url = reverse_lazy("students:list")

# Student Delete View
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("students:list")
