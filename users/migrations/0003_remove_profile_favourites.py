# Generated by Django 2.1.5 on 2019-02-18 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favourites',
        ),
    ]
