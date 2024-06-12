from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.form import MailingLettersForm, ModeratorFormMailing
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


class MailingLettersListView(LoginRequiredMixin, ListView):

    model = MailingLetters
    template_name = 'mailing/mailings.html'
    login_url = 'users:login'

    def get_queryset(self):
        return MailingLetters.objects.filter(owner=self.request.user)


class MailingLettersCreateView(LoginRequiredMixin, FromValidMixin, CreateView):

    model = MailingLetters
    form_class = MailingLettersForm
    success_url = reverse_lazy('mailing:mailings')
    login_url = 'users:login'


class MailingLettersDetailView(LoginRequiredMixin, DetailView):

    model = MailingLetters
    template_name = 'mailing/mailing_detail.html'
    login_url = 'users:login'


class MailingLettersUpdateView(LoginRequiredMixin, FromValidMixin, UpdateView):

    model = MailingLetters
    form_class = MailingLettersForm
    success_url = reverse_lazy('mailing:mailings')

    def test_func(self):
        if self.request.user.has_perms(
                ('status',)
        ) or (self.get_object().owner == self.request.user):
            return True
        return self.handle_no_permission()

    def get_form_class(self):
        if self.request.user.groups.filter(name="moderator"):
            return ModeratorFormMailing
        if self.request.user == self.get_object().owner:
            return MailingLettersForm


class MailingLettersDeleteView(UserPassesTestMixin, DeleteView):

    model = MailingLetters
    success_url = reverse_lazy('mailing:mailings')
