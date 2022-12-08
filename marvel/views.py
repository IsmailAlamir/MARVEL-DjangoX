from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Marvel


class MarvelListView(ListView):
    template_name = "marvel/marvel-list.html"
    model = Marvel


class MarvelDetailView(DetailView):
    template_name = "marvel/marvel-detail.html"
    model = Marvel


class MarvelCreateView(CreateView):
    template_name = "marvel/marvel-create.html"
    model = Marvel
    fields = ['name','character','description','image']


class MarvelUpdateView(UpdateView):
    template_name = "marvel/marvel-update.html"
    model = Marvel
    fields = ['name','character','description','image']


class MarvelDeleteView(DeleteView):
    template_name = "marvel/marvel-delete.html"
    model = Marvel
    success_url = reverse_lazy("marvel_list")
