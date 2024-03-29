# Generated by Django 2.1.5 on 2019-03-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_auto_20190304_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_availability',
            new_name='is_available',
        ),
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('MV', 'Mvita'), ('LM', 'Limuru'), ('RK', 'Ruaka'), ('SA', 'Kisauni'), ('KU', 'Kikuyu'), ('LO', 'Loresho'), ('LV', 'Lavington'), ('NL', 'Nyali'), ('TH', 'Kithiani'), ('SY', 'Syokimau'), ('KW', 'Kwale'), ('SU', 'Kahawa Sukari'), ('JJ', 'Juja'), ('LK', 'Likoni'), ('KB', 'Kabete'), ('KK', 'Kakamega'), ('WT', 'Watamu'), ('BU', 'Bungoma'), ('KT', 'Kitengela'), ('NR', 'Narok'), ('LE', 'Kileleshwa'), ('OR', 'Ongata Rongai'), ('KI', 'Kisii'), ('EL', 'Eldoret'), ('NH', 'Nyahururu'), ('KM', 'Kiambu'), ('KS', 'Kiserian'), ('NY', 'Nyamira'), ('IS', 'Isinya'), ('NE', 'Nyeri'), ('LI', 'Kilimani'), ('NV', 'Naivasha'), ('MS', 'Mombasa'), ('KR', 'Karen'), ('NA', 'Nakuru'), ('ND', 'Nyandarua'), ('RU', 'Ruiru'), ('WS', 'Kahawa West'), ('MK', 'Mavoko'), ('MC', 'Machakos'), ('KA', 'Kajiado'), ('MA', 'Malindi'), ('NG', 'Namanga'), ('AR', 'Athi River'), ('WN', 'Kahawa Wendani'), ('DA', 'Dagoretti'), ('MW', 'Msambweni'), ('NU', 'Nyanyuki'), ('WE', 'Westlands'), ('UK', 'Ukunda'), ('KN', 'Kinoo'), ('LA', 'Langata'), ('KL', 'Kilifi')], max_length=2),
        ),
    ]
