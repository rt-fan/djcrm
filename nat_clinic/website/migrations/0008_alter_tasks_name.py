# Generated by Django 3.2.19 on 2023-05-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20230513_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
    ]
