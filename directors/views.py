from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Director
from .forms import DirectorForm


class DirectorListView(ListView):
    model = Director
    template_name = 'directors/directors_list.html'
    context_object_name = 'directors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Directors"
        return context


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directors/director_detail.html'
    context_object_name = 'director'


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directors/director_form.html'
    success_url = reverse_lazy('directors:list')


class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directors/director_form.html'
    success_url = reverse_lazy('directors:list')


class DirectorDeleteView(DeleteView):
    model = Director
    template_name = 'directors/director_confirm_delete.html'
    success_url = reverse_lazy('directors:list')
