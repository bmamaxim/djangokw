from django.contrib.auth.models import AbstractUser
from django.db import models

from client.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='элктронная почта')
    ver_code = models.CharField(max_length=4, verbose_name='код верификации', **NULLABLE)
    user_activ = models.BooleanField(default=True, verbose_name='активный пользователь')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата записи', **NULLABLE)
    updated_at = models.DateField(auto_now_add=True, verbose_name='последние изменения', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

        permissions = (
            (
                'user_activ',
                'Блокировка пользователя'
            ),
        )
