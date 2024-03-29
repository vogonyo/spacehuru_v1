# Generated by Django 2.1.5 on 2019-02-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20190214_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('NG', 'Namanga'), ('NU', 'Nyanyuki'), ('NL', 'Nyali'), ('NH', 'Nyahururu'), ('NA', 'Nakuru'), ('NE', 'Nyeri'), ('LI', 'Kilimani'), ('TH', 'Kithiani'), ('KL', 'Kilifi'), ('KN', 'Kinoo'), ('KB', 'Kabete'), ('LM', 'Limuru'), ('KU', 'Kikuyu'), ('UK', 'Ukunda'), ('SU', 'Kahawa Sukari'), ('KS', 'Kiserian'), ('SY', 'Syokimau'), ('RK', 'Ruaka'), ('RU', 'Ruiru'), ('WS', 'Kahawa West'), ('BU', 'Bungoma'), ('MV', 'Mvita'), ('AR', 'Athi River'), ('LO', 'Loresho'), ('JJ', 'Juja'), ('EL', 'Eldoret'), ('WT', 'Watamu'), ('NV', 'Naivasha'), ('LA', 'Langata'), ('LV', 'Lavington'), ('ND', 'Nyandarua'), ('IS', 'Isinya'), ('SA', 'Kisauni'), ('MS', 'Mombasa'), ('MK', 'Mavoko'), ('KA', 'Kajiado'), ('DA', 'Dagoretti'), ('WN', 'Kahawa Wendani'), ('KM', 'Kiambu'), ('MC', 'Machakos'), ('WE', 'Westlands'), ('KR', 'Karen'), ('KK', 'Kakamega'), ('KW', 'Kwale'), ('KT', 'Kitengela'), ('MA', 'Malindi'), ('MW', 'Msambweni'), ('NY', 'Nyamira'), ('KI', 'Kisii'), ('NR', 'Narok'), ('OR', 'Ongata Rongai'), ('LE', 'Kileleshwa'), ('LK', 'Likoni')], max_length=2),
        ),
    ]
