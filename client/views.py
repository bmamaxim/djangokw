from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):

    model = Client
    template_name = 'client/home.html'


class ClientCreateView(CreateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:home')


class ClientDetailView(DetailView):

    model = Client
    template_name = 'client/client_detail.html'


class ClientUpdateView(UpdateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:home')


class ClientDeleteView(DeleteView):

    model = Client
    success_url = reverse_lazy('client:home')
