from django.db import models

from client.models import NULLABLE, Client
from config import settings



class Letter(models.Model):

    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='писатель')
    subject = models.CharField(max_length=500, verbose_name='тема письма', **NULLABLE)
    body = models.CharField(verbose_name='тема письма', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата записи')
    updated_at = models.DateField(auto_now_add=True, verbose_name='последние изменения')

    def __str__(self):
        return f"{self.subject} {self.body}"

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


