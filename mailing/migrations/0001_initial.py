# Generated by Django 4.2 on 2024-05-12 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letter', '0003_alter_letter_body'),
        ('client', '0002_client_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingLetters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='начало рассылки')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='начало рассылки')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', ' Еженедельная'), ('monthly', 'Ежемесячная')], default='daily', max_length=50, verbose_name='период')),
                ('status', models.CharField(choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], default='started', max_length=50, verbose_name='статус')),
                ('clients', models.ManyToManyField(related_name='settings', to='client.client')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='letter.letter', verbose_name='сообщение')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]
