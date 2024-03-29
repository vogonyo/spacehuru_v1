# Generated by Django 2.1.5 on 2019-03-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_auto_20190228_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='maxPrice',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='minPrice',
        ),
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('TH', 'Kithiani'), ('KU', 'Kikuyu'), ('NU', 'Nyanyuki'), ('NV', 'Naivasha'), ('LK', 'Likoni'), ('LM', 'Limuru'), ('AR', 'Athi River'), ('IS', 'Isinya'), ('KW', 'Kwale'), ('WE', 'Westlands'), ('KB', 'Kabete'), ('OR', 'Ongata Rongai'), ('EL', 'Eldoret'), ('RK', 'Ruaka'), ('UK', 'Ukunda'), ('KM', 'Kiambu'), ('WT', 'Watamu'), ('LI', 'Kilimani'), ('LV', 'Lavington'), ('KT', 'Kitengela'), ('MS', 'Mombasa'), ('MK', 'Mavoko'), ('WN', 'Kahawa Wendani'), ('KK', 'Kakamega'), ('MC', 'Machakos'), ('SY', 'Syokimau'), ('NE', 'Nyeri'), ('NH', 'Nyahururu'), ('ND', 'Nyandarua'), ('MV', 'Mvita'), ('SA', 'Kisauni'), ('KL', 'Kilifi'), ('BU', 'Bungoma'), ('MA', 'Malindi'), ('KA', 'Kajiado'), ('LE', 'Kileleshwa'), ('LA', 'Langata'), ('KR', 'Karen'), ('NY', 'Nyamira'), ('KS', 'Kiserian'), ('DA', 'Dagoretti'), ('RU', 'Ruiru'), ('WS', 'Kahawa West'), ('NG', 'Namanga'), ('NL', 'Nyali'), ('MW', 'Msambweni'), ('KI', 'Kisii'), ('SU', 'Kahawa Sukari'), ('JJ', 'Juja'), ('KN', 'Kinoo'), ('LO', 'Loresho'), ('NA', 'Nakuru'), ('NR', 'Narok')], max_length=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='billing',
            field=models.CharField(blank=True, choices=[('HR', 'Hour'), ('DY', 'Day'), ('MT', 'Month'), ('WK', 'Week'), ('DK', 'Desk')], max_length=200),
        ),
    ]
