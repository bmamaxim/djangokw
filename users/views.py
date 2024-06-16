import random

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, DeleteView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify')

    def form_valid(self, form):
        user = form.save()
        current_site = self.request.get_host()
        ver_code = ''.join([str(random.randint(1, 9)) for _ in range(4)])
        user.ver_code = ver_code
        user.is_active = False
        user.save()
        send_mail(
            subject='Верификация',
            message=f'код для входа: {ver_code}\n в {current_site}/users/verify',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class Verify(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/verification.html')

    def post(self, request, *args, **kwargs):
        code = request.POST.get('ver_code')
        user = get_object_or_404(User, ver_code=code)

        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect('users:login')
        return redirect('/')


class ProfileView(UpdateView):

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RestoreView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/recovery_pass.html')

    def post(self, request, *args, **kwargs):
        mail = request.POST.get('email')
        user = get_object_or_404(User, email=mail)
        restore_pass = ''.join([str(random.randint(1, 9)) for _ in range(4)])
        send_mail(
            subject='пароль',
            message=f'пароль для входа: {restore_pass}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(restore_pass)
        user.save()
        return redirect('users:login')


class UserListView(ListView):

    model = User
    template_name = 'users/users.html'


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'users/detail.html'


class UserDeleteView(UserPassesTestMixin, DeleteView):

    model = User
    success_url = reverse_lazy('users:list')


@login_required
@permission_required('users.user_activ')
def toggle_activity(reqwest, pk):
    """
    Функция меняет статус пользователя
    активен/не активен
    :param reqwest:
    :param pk:
    :return:
    """
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(reverse('users:list'))
