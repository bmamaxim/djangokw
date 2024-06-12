from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from letter.form import LettersForm
from letter.models import Letter
from mailing.form import MailingLettersForm
from mailing.models import MailingLetters


class LetterCreateView(LoginRequiredMixin, CreateView):
    """
    Класс создания письма рассылки
    с методом привязки к пользователю
    """
    model = Letter
    form_class = LettersForm
    success_url = reverse_lazy('letter:letters')

    def form_valid(self, form):
        self.object = form.save()
        self.object.writer = self.request.user
        self.object.save()

        return super().form_valid(form)


class LetterListView(LoginRequiredMixin, ListView):
    """
    Список писем
    """
    model = Letter
    template_name = 'letter/letters.html'

class LetterDetailView(UserPassesTestMixin, DetailView):
    """
    Просмотр письма
    """
    model = Letter

    def test_func(self):
        if self.get_object().writer == self.request.user:
            return True
        return self.handle_no_permission()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['formset'] = MailingLetters.objects.all()
        #if not self.request.user.groups.filter(name='moderator'):
        #VersionFormset = inlineformset_factory(Letter, MailingLetters, form=MailingLettersForm, extra=1)
        #if self.request.method == 'POST':
            #context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        #else:
            #context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

class LetterUpdateView(UserPassesTestMixin, UpdateView):
    """
    Класс изменения письма
    """
    model = Letter
    form_class = LettersForm
    success_url = reverse_lazy('letter:letters')

    def test_func(self):
        if self.get_object().writer == self.request.user:
            return True
        return self.handle_no_permission()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['formset'] = MailingLetters.objects.all()
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.writer = self.request.user
        self.object.save()

        return super().form_valid(form)


class LetterDeleteView(UserPassesTestMixin, DeleteView):
    """
    Класс удаления письма
    """
    model = Letter
    success_url = reverse_lazy('letter:letters')

    def test_func(self):
        if self.get_object().writer == self.request.user:
            return True
        return self.handle_no_permission()
