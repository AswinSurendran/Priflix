# Generated by Django 4.2.5 on 2023-10-27 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_rename_music_categories_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='movie',
        ),
    ]
