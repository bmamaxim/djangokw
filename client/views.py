from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):

    model = Client
    template_name = 'client/home.html'


class ClientCreateView(CreateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:home')