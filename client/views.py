from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):

    model = Client
    template_name = 'client/clients.html'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user.id)


class ClientCreateView(CreateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientDetailView(DetailView):

    model = Client
    template_name = 'client/client_detail.html'


class ClientUpdateView(UpdateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:clients')


class ClientDeleteView(DeleteView):

    model = Client
    success_url = reverse_lazy('client:clients')
