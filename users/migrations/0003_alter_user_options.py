# Generated by Django 4.2 on 2024-06-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('ban', 'Блокировка пользователя'),), 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]