# Generated by Django 4.2 on 2024-05-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='элктронная почта')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О')),
                ('comment', models.CharField(blank=True, null=True, verbose_name='комментарий')),
                ('publication_sign', models.BooleanField(default=True, verbose_name='публикация')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='дата записи')),
                ('updated_at', models.DateField(auto_now_add=True, null=True, verbose_name='последние изменения')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]
