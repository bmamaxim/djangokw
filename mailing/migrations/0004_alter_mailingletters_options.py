# Generated by Django 4.2 on 2024-06-12 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_mailingletters_start'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingletters',
            options={'permissions': (('status', 'изменение статуса'),), 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
