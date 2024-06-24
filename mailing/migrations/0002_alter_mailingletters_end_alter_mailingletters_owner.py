# Generated by Django 4.2 on 2024-06-09 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingletters',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='конец рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingletters',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
