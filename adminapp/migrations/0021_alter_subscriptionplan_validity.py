# Generated by Django 4.2.5 on 2023-11-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_alter_subscriptionplan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='validity',
            field=models.IntegerField(max_length=20),
        ),
    ]
