from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Teacher
from subjects.models import Subject
from departments.models import Department
from .forms import TeacherForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'
    paginate_by = 10

    def get_queryset(self):
        queryset = Teacher.objects.all()
        department = self.request.GET.get('department')
        subject = self.request.GET.get('subject')
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
            )

        if department and department != "All":
            queryset = queryset.filter(department__name=department)

        if subject and subject != "All":
            queryset = queryset.filter(subjects__name=subject)

        if status and status != "Status":
            if status == "Active":
                queryset = queryset.filter(is_active=True)
            elif status == "On Leave":
                queryset = queryset.filter(is_active=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['subjects'] = Subject.objects.all()
        context["title"] = "Teachers"
        context['search_query'] = self.request.GET.get('q', '')  # Qidiruv so'zini kontekstga qo'shish
        return context


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Teacher,
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('teachers:list')
