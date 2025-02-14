from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GroupForm
from django.db.models import Q
from .models import Group, Teacher


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = "groups/list.html"
    context_object_name = "groups"

    def get_queryset(self):
        queryset = Group.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        grade = self.request.GET.get("grade")
        if grade:
            queryset = queryset.filter(grade_level=grade)
        schedule = self.request.GET.get("schedule")
        if schedule:
            queryset = queryset.filter(schedule=schedule)
        teacher_id = self.request.GET.get("teacher")
        if teacher_id:
            queryset = queryset.filter(teachers__id=teacher_id)
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Groups"
        context["grade_choices"] = Group.GRADE_LEVEL_CHOICES
        context["schedule_choices"] = Group.SCHEDULE_CHOICES
        context["teachers"] = Teacher.objects.all()
        return context




class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = "groups/detail.html"
    context_object_name = "group"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Group,
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors'] = Group.objects.all()
        return context


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/form.html"


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = "groups/group_confirm_delete.html"
    success_url = reverse_lazy("groups:list")
