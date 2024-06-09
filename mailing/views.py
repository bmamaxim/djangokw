from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.form import MailingLettersForm
from mailing.models import MailingLetters



class FromValidMixin:


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingLettersListView(ListView):

    model = MailingLetters
    template_name = 'mailing/mailings.html'

    def get_queryset(self):
        return MailingLetters.objects.filter(owner=self.request.user)


class MailingLettersCreateView(FromValidMixin, CreateView):

    model = MailingLetters
    form_class = MailingLettersForm
    success_url = reverse_lazy('mailing:mailings')



class MailingLettersDetailView(DetailView):

    model = MailingLetters
    template_name = 'mailing/mailing_detail.html'


class MailingLettersUpdateView(FromValidMixin, UpdateView):

    model = MailingLetters
    form_class = MailingLettersForm
    success_url = reverse_lazy('mailing:mailings')


class MailingLettersDeleteView(DeleteView):

    model = MailingLetters
    success_url = reverse_lazy('mailing:mailings')
