# Generated by Django 3.2.19 on 2023-05-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_clients_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]