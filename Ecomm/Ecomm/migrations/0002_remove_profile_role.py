# Generated by Django 5.0.2 on 2024-03-10 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
    ]
