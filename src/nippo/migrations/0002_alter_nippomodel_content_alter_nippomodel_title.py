# Generated by Django 5.1.4 on 2025-01-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippomodel',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='nippomodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
