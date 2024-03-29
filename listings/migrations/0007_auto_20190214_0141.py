# Generated by Django 2.1.5 on 2019-02-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20190211_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('KT', 'Kitengela'), ('SA', 'Kisauni'), ('NH', 'Nyahururu'), ('LO', 'Loresho'), ('MW', 'Msambweni'), ('KB', 'Kabete'), ('NE', 'Nyeri'), ('AR', 'Athi River'), ('LA', 'Langata'), ('TH', 'Kithiani'), ('LM', 'Limuru'), ('KK', 'Kakamega'), ('MA', 'Malindi'), ('NG', 'Namanga'), ('RK', 'Ruaka'), ('MK', 'Mavoko'), ('SY', 'Syokimau'), ('WT', 'Watamu'), ('KL', 'Kilifi'), ('NY', 'Nyamira'), ('KW', 'Kwale'), ('WE', 'Westlands'), ('KR', 'Karen'), ('RU', 'Ruiru'), ('LE', 'Kileleshwa'), ('KI', 'Kisii'), ('NR', 'Narok'), ('JJ', 'Juja'), ('LV', 'Lavington'), ('BU', 'Bungoma'), ('NV', 'Naivasha'), ('NA', 'Nakuru'), ('IS', 'Isinya'), ('KM', 'Kiambu'), ('MS', 'Mombasa'), ('EL', 'Eldoret'), ('UK', 'Ukunda'), ('ND', 'Nyandarua'), ('WS', 'Kahawa West'), ('LI', 'Kilimani'), ('KN', 'Kinoo'), ('KA', 'Kajiado'), ('DA', 'Dagoretti'), ('OR', 'Ongata Rongai'), ('LK', 'Likoni'), ('WN', 'Kahawa Wendani'), ('SU', 'Kahawa Sukari'), ('MV', 'Mvita'), ('MC', 'Machakos'), ('NU', 'Nyanyuki'), ('KU', 'Kikuyu'), ('NL', 'Nyali'), ('KS', 'Kiserian')], max_length=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, verbose_name='date created'),
        ),
    ]
