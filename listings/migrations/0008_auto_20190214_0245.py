# Generated by Django 2.1.5 on 2019-02-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20190214_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('LO', 'Loresho'), ('KW', 'Kwale'), ('KL', 'Kilifi'), ('KM', 'Kiambu'), ('LM', 'Limuru'), ('IS', 'Isinya'), ('MW', 'Msambweni'), ('SU', 'Kahawa Sukari'), ('KI', 'Kisii'), ('SA', 'Kisauni'), ('NG', 'Namanga'), ('KK', 'Kakamega'), ('NH', 'Nyahururu'), ('LV', 'Lavington'), ('KB', 'Kabete'), ('KU', 'Kikuyu'), ('KN', 'Kinoo'), ('LA', 'Langata'), ('SY', 'Syokimau'), ('WN', 'Kahawa Wendani'), ('OR', 'Ongata Rongai'), ('EL', 'Eldoret'), ('MK', 'Mavoko'), ('NA', 'Nakuru'), ('JJ', 'Juja'), ('MS', 'Mombasa'), ('KS', 'Kiserian'), ('DA', 'Dagoretti'), ('MV', 'Mvita'), ('RU', 'Ruiru'), ('LI', 'Kilimani'), ('KT', 'Kitengela'), ('NY', 'Nyamira'), ('WT', 'Watamu'), ('NV', 'Naivasha'), ('UK', 'Ukunda'), ('LE', 'Kileleshwa'), ('TH', 'Kithiani'), ('WE', 'Westlands'), ('NE', 'Nyeri'), ('NR', 'Narok'), ('NU', 'Nyanyuki'), ('MA', 'Malindi'), ('WS', 'Kahawa West'), ('KA', 'Kajiado'), ('LK', 'Likoni'), ('AR', 'Athi River'), ('BU', 'Bungoma'), ('MC', 'Machakos'), ('KR', 'Karen'), ('NL', 'Nyali'), ('RK', 'Ruaka'), ('ND', 'Nyandarua')], max_length=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
    ]
