from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from letter.form import LettersForm
from letter.models import Letter
from mailing.form import MailingLettersForm
from mailing.models import MailingLetters


class LetterCreateView(CreateView):
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


class LetterListView(ListView):
    """
    Список писем
    """
    model = Letter
    template_name = 'letter/letters.html'

class LetterDetailView(DetailView):
    """
    Просмотр письма
    """
    model = Letter

class LetterUpdateView(UpdateView):
    """
    Класс изменения письма
    """
    model = Letter
    form_class = LettersForm
    success_url = reverse_lazy('letter:letters')

    def form_valid(self, form):
        self.object = form.save()
        self.object.writer = self.request.user
        self.object.save()

        return super().form_valid(form)


class LetterDeleteView(DeleteView):
    """
    Класс удаления письма
    """
    model = Letter
    success_url = reverse_lazy('letter:letters')
