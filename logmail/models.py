from django.db import models

from client.models import Client, NULLABLE
from mailing.models import MailingLetters


class LogMail(models.Model):

    STATUS_SUCCESS = 'success'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_SUCCESS, 'Успешно'),
        (STATUS_FAILED, 'Ошибка')
    )

    last_try = models.DateTimeField(auto_now_add=True, verbose_name='последняя рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    settings = models.ForeignKey(MailingLetters, on_delete=models.SET_NULL, verbose_name='настройки', **NULLABLE)
    status = models.CharField(choices=STATUSES, default=STATUS_SUCCESS, verbose_name='статус')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
