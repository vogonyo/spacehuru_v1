# Generated by Django 2.1.5 on 2019-03-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0033_auto_20190306_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('NY', 'Nyamira'), ('WN', 'Kahawa Wendani'), ('KB', 'Kabete'), ('NE', 'Nyeri'), ('KA', 'Kajiado'), ('SA', 'Kisauni'), ('KS', 'Kiserian'), ('LA', 'Langata'), ('LE', 'Kileleshwa'), ('UK', 'Ukunda'), ('DA', 'Dagoretti'), ('RU', 'Ruiru'), ('KL', 'Kilifi'), ('NU', 'Nyanyuki'), ('NR', 'Narok'), ('KK', 'Kakamega'), ('SY', 'Syokimau'), ('JJ', 'Juja'), ('MA', 'Malindi'), ('BU', 'Bungoma'), ('LV', 'Lavington'), ('MS', 'Mombasa'), ('ND', 'Nyandarua'), ('LI', 'Kilimani'), ('MV', 'Mvita'), ('KR', 'Karen'), ('EL', 'Eldoret'), ('RK', 'Ruaka'), ('MC', 'Machakos'), ('TH', 'Kithiani'), ('WS', 'Kahawa West'), ('NG', 'Namanga'), ('NL', 'Nyali'), ('KN', 'Kinoo'), ('LM', 'Limuru'), ('LK', 'Likoni'), ('KU', 'Kikuyu'), ('MW', 'Msambweni'), ('KM', 'Kiambu'), ('NA', 'Nakuru'), ('IS', 'Isinya'), ('LO', 'Loresho'), ('NH', 'Nyahururu'), ('WT', 'Watamu'), ('KT', 'Kitengela'), ('MK', 'Mavoko'), ('KI', 'Kisii'), ('AR', 'Athi River'), ('SU', 'Kahawa Sukari'), ('KW', 'Kwale'), ('WE', 'Westlands'), ('OR', 'Ongata Rongai'), ('NV', 'Naivasha')], max_length=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='used_for',
            field=models.CharField(choices=[('AC', 'Accommodation & Housing'), ('SH', 'Shopping'), ('FO', 'Food & Drink'), ('FU', 'Fun & Experiences'), ('WE', 'Health & Wellness'), ('PA', 'Parking'), ('NL', 'Nightlife'), ('SE', 'Social Events'), ('CE', 'Corporate Events'), ('WD', 'Weddings'), ('RE', 'Retail Shops'), ('CA', 'Camping'), ('TR', 'Travel & Hospitality'), ('ET', 'Entertainment'), ('ME', 'MeetUps and Meetings'), ('OF', 'Office & Co-Working'), ('OT', 'Other Uses')], default='Other', max_length=200),
        ),
    ]
