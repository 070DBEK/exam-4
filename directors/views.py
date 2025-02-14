from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Director
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import DirectorForm


class DirectorListView(LoginRequiredMixin, ListView):
    model = Director
    template_name = "directors/list.html"
    context_object_name = "directors"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(bio__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Directors"
        context["search_query"] = self.request.GET.get("q", "")
        return context


class DirectorDetailView(LoginRequiredMixin, DetailView):
    model = Director
    template_name = 'directors/detail.html'
    context_object_name = 'director'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Director,
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )


class DirectorCreateView(LoginRequiredMixin, CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directors/form.html'
    success_url = reverse_lazy('directors:list')


class DirectorUpdateView(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directors/form.html'
    success_url = reverse_lazy('directors:list')


class DirectorDeleteView(LoginRequiredMixin, DeleteView):
    model = Director
    template_name = 'directors/director_confirm_delete.html'
    success_url = reverse_lazy('directors:list')
