from django.db import models

from client.models import NULLABLE, Client
from config import settings
from letter.models import Letter


class MailingLetters(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, ' Еженедельная'),
        (PERIOD_MONTHLY, 'Ежемесячная'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена')
    )

    start = models.DateTimeField(verbose_name='начало рассылки')
    end = models.DateTimeField(verbose_name='начало рассылки', **NULLABLE)
    period = models.CharField(max_length=50, choices=PERIODS, default=PERIOD_DAILY, verbose_name='период')
    status = models.CharField(max_length=50, choices=STATUSES, default=STATUS_STARTED, verbose_name='статус')
    message = models.ForeignKey(Letter, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, related_name='settings')

    def __str__(self):
        return (f"{self.start} "
                f"{self.period} "
                f"{self.status}")

    class Meta:

        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
