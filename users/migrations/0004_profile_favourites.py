# Generated by Django 2.1.5 on 2019-02-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_auto_20190221_2058'),
        ('users', '0003_remove_profile_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(related_name='favorited_by', to='listings.Listing'),
        ),
    ]
