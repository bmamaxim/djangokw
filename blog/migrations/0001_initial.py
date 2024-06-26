# Generated by Django 4.2 on 2024-05-19 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='изображение')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='дата публикации')),
                ('publication_sign', models.BooleanField(default=True, verbose_name='публикация')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='писатель')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
