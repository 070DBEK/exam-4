from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department
from .forms import DepartmentForm


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Departments"
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/confirm_delete.html'
    success_url = reverse_lazy('departments:list')
