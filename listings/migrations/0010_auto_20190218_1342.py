# Generated by Django 2.1.5 on 2019-02-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20190217_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('WT', 'Watamu'), ('ND', 'Nyandarua'), ('BU', 'Bungoma'), ('LO', 'Loresho'), ('NA', 'Nakuru'), ('MS', 'Mombasa'), ('KM', 'Kiambu'), ('KA', 'Kajiado'), ('NU', 'Nyanyuki'), ('LI', 'Kilimani'), ('SY', 'Syokimau'), ('RU', 'Ruiru'), ('JJ', 'Juja'), ('IS', 'Isinya'), ('AR', 'Athi River'), ('NR', 'Narok'), ('DA', 'Dagoretti'), ('KU', 'Kikuyu'), ('WN', 'Kahawa Wendani'), ('SA', 'Kisauni'), ('NE', 'Nyeri'), ('MV', 'Mvita'), ('UK', 'Ukunda'), ('MK', 'Mavoko'), ('KK', 'Kakamega'), ('NL', 'Nyali'), ('NH', 'Nyahururu'), ('SU', 'Kahawa Sukari'), ('KS', 'Kiserian'), ('KR', 'Karen'), ('KL', 'Kilifi'), ('MW', 'Msambweni'), ('LV', 'Lavington'), ('NV', 'Naivasha'), ('NG', 'Namanga'), ('TH', 'Kithiani'), ('KN', 'Kinoo'), ('KB', 'Kabete'), ('EL', 'Eldoret'), ('NY', 'Nyamira'), ('MA', 'Malindi'), ('LA', 'Langata'), ('LM', 'Limuru'), ('KI', 'Kisii'), ('KT', 'Kitengela'), ('OR', 'Ongata Rongai'), ('LE', 'Kileleshwa'), ('RK', 'Ruaka'), ('MC', 'Machakos'), ('WE', 'Westlands'), ('WS', 'Kahawa West'), ('KW', 'Kwale'), ('LK', 'Likoni')], max_length=2),
        ),
    ]
