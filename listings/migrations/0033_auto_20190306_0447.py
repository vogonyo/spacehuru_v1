# Generated by Django 2.1.5 on 2019-03-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0032_auto_20190306_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('LM', 'Limuru'), ('UK', 'Ukunda'), ('LO', 'Loresho'), ('DA', 'Dagoretti'), ('SY', 'Syokimau'), ('OR', 'Ongata Rongai'), ('MC', 'Machakos'), ('NH', 'Nyahururu'), ('KM', 'Kiambu'), ('SU', 'Kahawa Sukari'), ('NL', 'Nyali'), ('KB', 'Kabete'), ('ND', 'Nyandarua'), ('NA', 'Nakuru'), ('NY', 'Nyamira'), ('MV', 'Mvita'), ('IS', 'Isinya'), ('KN', 'Kinoo'), ('LK', 'Likoni'), ('JJ', 'Juja'), ('KW', 'Kwale'), ('NG', 'Namanga'), ('MA', 'Malindi'), ('LE', 'Kileleshwa'), ('WT', 'Watamu'), ('KK', 'Kakamega'), ('MS', 'Mombasa'), ('KI', 'Kisii'), ('KR', 'Karen'), ('NU', 'Nyanyuki'), ('LA', 'Langata'), ('MK', 'Mavoko'), ('WN', 'Kahawa Wendani'), ('NV', 'Naivasha'), ('WE', 'Westlands'), ('BU', 'Bungoma'), ('LI', 'Kilimani'), ('RU', 'Ruiru'), ('LV', 'Lavington'), ('NR', 'Narok'), ('SA', 'Kisauni'), ('EL', 'Eldoret'), ('NE', 'Nyeri'), ('MW', 'Msambweni'), ('AR', 'Athi River'), ('KU', 'Kikuyu'), ('KA', 'Kajiado'), ('WS', 'Kahawa West'), ('KL', 'Kilifi'), ('RK', 'Ruaka'), ('KT', 'Kitengela'), ('KS', 'Kiserian'), ('TH', 'Kithiani')], max_length=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='used_for',
            field=models.CharField(choices=[('AC', 'Accommodation & Housing'), ('SH', 'Shopping'), ('FO', 'Food & Drink'), ('FU', 'Fun & Experiences'), ('WE', 'Health & Wellness'), ('PA', 'Parking'), ('NL', 'Nightlife'), ('SE', 'Social Events'), ('CE', 'Corporate Events'), ('WD', 'Weddings'), ('RE', 'Retail Shops'), ('CA', 'Camping'), ('TR', 'Travel & Hospitality'), ('ET', 'Entertainment'), ('ME', 'MeetUps and Meetings'), ('OF', 'Office & Co-Working')], default='Other', max_length=200),
        ),
    ]
