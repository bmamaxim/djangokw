from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from client.models import Client
from logmail.form import LogMailForm
from logmail.models import LogMail
from mailing.form import MailingLettersForm
from mailing.models import MailingLetters



class FromValidMixin:
    """
    Класс миксин валидации пользователя
    """
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingLettersListView(LoginRequiredMixin, ListView):

    model = MailingLetters
    template_name = 'mailing/mailings.html'
    login_url = 'users:login'

    def get_queryset(self):
        if self.request.user.groups.filter(name="moderator"):
            print(self.request.user.groups)
            return MailingLetters.objects.all()
        return MailingLetters.objects.filter(owner=self.request.user)


class MailingLettersCreateView(FromValidMixin, CreateView):

    model = MailingLetters
    form_class = MailingLettersForm
    success_url = reverse_lazy('mailing:mailings')
    login_url = 'users:login'


class MailingLettersDetailView(LoginRequiredMixin, DetailView):

    model = MailingLetters
    template_name = 'mailing/mailing_detail.html'
    login_url = 'users:login'

    def get_queryset(self):
        return MailingLetters.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Информация по рассылкам'
        context_data['mailings_all'] = len(LogMail.objects.all())
        context_data['mailings_started'] = len(MailingLetters.objects.filter(status='started'))
        context_data['mailings_clients'] = len(Client.objects.filter(owner=self.request.user))
        return context_data


class MailingLettersUpdateView(UserPassesTestMixin, FromValidMixin, UpdateView):

    model = MailingLetters
    form_class = MailingLettersForm
    success_url = reverse_lazy('mailing:mailings')

    def test_func(self):
        if self.get_object().owner == self.request.user:
            return True
        return self.handle_no_permission()



class MailingLettersDeleteView(UserPassesTestMixin, DeleteView):

    model = MailingLetters
    success_url = reverse_lazy('mailing:mailings')

    def test_func(self):
        if self.get_object().owner == self.request.user:
            return True
        return self.handle_no_permission()


@login_required
@permission_required('mailing.status')
def mailing_status(reqwest, pk):
    mailing = get_object_or_404(MailingLetters, pk=pk)
    if mailing.status:
        mailing.status = 'done'
    mailing.save()
    return redirect(reverse('mailing:mailings'))
