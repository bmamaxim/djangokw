from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from letter.form import LettersForm
from letter.models import Letter


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

    def get_queryset(self):
        return Letter.objects.filter(writer=self.request.user)


class LetterDetailView(UserPassesTestMixin, DetailView):
    """
    Просмотр письма
    """
    model = Letter

    def test_func(self):
        if self.get_object().writer == self.request.user:
            return True
        return self.handle_no_permission()


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
