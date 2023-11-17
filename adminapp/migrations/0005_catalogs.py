# Generated by Django 4.2.5 on 2023-10-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_categories_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=20)),
                ('watched', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
    ]
