# Generated by Django 2.1.5 on 2019-02-10 09:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('AP', 'Apartments'), ('LD', 'Land'), ('CO', 'Coworking'), ('HO', 'Homes'), ('OF', 'Offices'), ('ST', 'Studios'), ('WR', 'Warehouses'), ('SH', 'Shops')], max_length=255)),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('area', models.CharField(choices=[('NV', 'Naivasha'), ('MS', 'Mombasa'), ('DA', 'Dagoretti'), ('WE', 'Westlands'), ('BU', 'Bungoma'), ('KB', 'Kabete'), ('AR', 'Athi River'), ('KM', 'Kiambu'), ('JJ', 'Juja'), ('LM', 'Limuru'), ('NU', 'Nyanyuki'), ('NL', 'Nyali'), ('ND', 'Nyandarua'), ('KS', 'Kiserian'), ('KI', 'Kisii'), ('NH', 'Nyahururu'), ('TH', 'Kithiani'), ('KW', 'Kwale'), ('WS', 'Kahawa West'), ('RU', 'Ruiru'), ('WT', 'Watamu'), ('NY', 'Nyamira'), ('LA', 'Langata'), ('LO', 'Loresho'), ('MK', 'Mavoko'), ('KU', 'Kikuyu'), ('LI', 'Kilimani'), ('RK', 'Ruaka'), ('KR', 'Karen'), ('WN', 'Kahawa Wendani'), ('UK', 'Ukunda'), ('LE', 'Kileleshwa'), ('NE', 'Nyeri'), ('LK', 'Likoni'), ('NR', 'Narok'), ('MW', 'Msambweni'), ('MA', 'Malindi'), ('MC', 'Machakos'), ('NA', 'Nakuru'), ('SY', 'Syokimau'), ('KK', 'Kakamega'), ('SA', 'Kisauni'), ('SU', 'Kahawa Sukari'), ('MV', 'Mvita'), ('IS', 'Isinya'), ('KN', 'Kinoo'), ('OR', 'Ongata Rongai'), ('EL', 'Eldoret'), ('KT', 'Kitengela'), ('KA', 'Kajiado'), ('NG', 'Namanga'), ('LV', 'Lavington'), ('KL', 'Kilifi')], max_length=2)),
                ('city', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('billing', models.CharField(blank=True, max_length=200)),
                ('minPrice', models.IntegerField(blank=True, default=0)),
                ('maxPrice', models.IntegerField(blank=True, default=0)),
                ('bedrooms', models.IntegerField(blank=True, default=0)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2)),
                ('sqft', models.IntegerField(blank=True, default=0)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=False)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
