# Generated by Django 4.2.5 on 2023-10-26 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='choose',
        ),
    ]