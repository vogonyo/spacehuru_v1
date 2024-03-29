# Generated by Django 2.1.5 on 2019-02-26 21:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0018_auto_20190226_1311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('WT', 'Watamu'), ('NV', 'Naivasha'), ('SU', 'Kahawa Sukari'), ('KR', 'Karen'), ('NL', 'Nyali'), ('NY', 'Nyamira'), ('JJ', 'Juja'), ('AR', 'Athi River'), ('KB', 'Kabete'), ('KA', 'Kajiado'), ('SY', 'Syokimau'), ('LE', 'Kileleshwa'), ('KT', 'Kitengela'), ('BU', 'Bungoma'), ('NE', 'Nyeri'), ('IS', 'Isinya'), ('LI', 'Kilimani'), ('NU', 'Nyanyuki'), ('KS', 'Kiserian'), ('LV', 'Lavington'), ('WS', 'Kahawa West'), ('LO', 'Loresho'), ('MC', 'Machakos'), ('EL', 'Eldoret'), ('NH', 'Nyahururu'), ('ND', 'Nyandarua'), ('KI', 'Kisii'), ('KN', 'Kinoo'), ('LM', 'Limuru'), ('KM', 'Kiambu'), ('KK', 'Kakamega'), ('TH', 'Kithiani'), ('LK', 'Likoni'), ('MA', 'Malindi'), ('SA', 'Kisauni'), ('LA', 'Langata'), ('RU', 'Ruiru'), ('RK', 'Ruaka'), ('KU', 'Kikuyu'), ('WN', 'Kahawa Wendani'), ('NR', 'Narok'), ('NG', 'Namanga'), ('NA', 'Nakuru'), ('MS', 'Mombasa'), ('MV', 'Mvita'), ('WE', 'Westlands'), ('MK', 'Mavoko'), ('KW', 'Kwale'), ('UK', 'Ukunda'), ('DA', 'Dagoretti'), ('OR', 'Ongata Rongai'), ('MW', 'Msambweni'), ('KL', 'Kilifi')], max_length=2),
        ),
    ]
