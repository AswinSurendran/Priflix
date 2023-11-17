# Generated by Django 4.2.5 on 2023-11-15 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flixapp', '0012_delete_subscriptionplan'),
        ('adminapp', '0021_alter_subscriptionplan_validity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribed_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='INACTIVE', max_length=100)),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminapp.subscriptionplan')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flixapp.register')),
            ],
        ),
    ]
