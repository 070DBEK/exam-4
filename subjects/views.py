from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Subject
from .forms import SubjectForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import render
from .models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = "subjects/list.html"
    context_object_name = "subjects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Directors"
        return context


class SubjectDetailView(DetailView):
    model = Subject
    template_name = "subjects/detail.html"
    context_object_name = "subject"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = self.get_object()
        context['total_groups'] = subject.groups.count()
        context["total_students"] = sum(group.students.count() for group in subject.groups.all())
        grades = [
            float(student.grade) for group in subject.groups.all()
            for student in group.students.all() if student.grade is not None
        ]
        context['average_grade'] = round(sum(grades) / len(grades), 2) if grades else "N/A"
        return context


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "subjects/subject_confirm_delete.html"
    success_url = reverse_lazy("subjects:list")


class SubjectCreateView(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, 'subjects/form.html', {'form': form})

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects:list')  # Subjects ro‘yxatiga qaytarish
        return render(request, 'subjects/form.html', {'form': form})


class SubjectUpdateView(View):
    def get(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk)
        form = SubjectForm(instance=subject)
        return render(request, 'subjects/form.html', {'form': form})

    def post(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects:list')
        return render(request, 'subjects/form.html', {'form': form})
