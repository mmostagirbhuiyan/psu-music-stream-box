# Generated by Django 3.0.8 on 2022-11-09 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_auto_20200712_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='language',
        ),
        migrations.RemoveField(
            model_name='song',
            name='singer',
        ),
        migrations.RemoveField(
            model_name='song',
            name='year',
        ),
    ]
