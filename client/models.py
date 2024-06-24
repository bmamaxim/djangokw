from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='элктронная почта')
    name = models.CharField(max_length=300, verbose_name='Ф.И.О', **NULLABLE)
    comment = models.CharField(verbose_name='комментарий', **NULLABLE)
    publication_sign = models.BooleanField(default=True, verbose_name='публикация')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата записи', **NULLABLE)
    updated_at = models.DateField(auto_now_add=True, verbose_name='последние изменения', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, **NULLABLE)

    def __str__(self):
        return (f'{self.email}'
                f'{self.name}')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
