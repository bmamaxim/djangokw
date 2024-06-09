from django.db import models

from client.models import NULLABLE
from config import settings


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='писатель')
    content = models.TextField(verbose_name='содержание', **NULLABLE)
    preview = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата публикации', **NULLABLE)
    publication_sign = models.BooleanField(default=True, verbose_name='публикация')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):
        return f"{self.title} {self.owner} {self.content}"


    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
