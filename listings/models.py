from django.db import models
import datetime, math
from realtors.models import Realtor
from django.contrib.auth.models import User
from .choices import city_choices
from django.urls import reverse
from django.utils.timezone import utc


 
class Listing(models.Model):
    # Area Choices
    WESTLANDS = 'WE'
    LIKONI = 'LK'
    KAHAWAWENDANI = 'WN'
    NAROK = 'NR'
    KILIMANI = 'LI'
    NAKURU = 'NA'
    DAGORETTI = 'DA'
    NYAMIRA = 'NY'
    RUAKA = 'RK'
    KAHAWASUKARI = 'SU'
    KISERIAN = 'KS'
    NAMANGA = 'NG'
    KISII = 'KI'
    LORESHO = 'LO'
    JUJA = 'JJ'
    KWALE = 'KW'
    WATAMU = 'WT'
    KITHIANI = 'TH'
    LIMURU = 'LM'
    MVITA = 'MV'
    KAJIADO = 'KA'
    KAREN = 'KR'
    KITENGELA = 'KT'
    LAVINGTON = 'LV'
    ATHIRIVER = 'AR'
    LANGATA = 'LA'
    ISINYA = 'IS'
    KISAUNI = 'SA'
    KILIFI = 'KL'
    SYOKIMAU = 'SY'
    ONGATARONGAI = 'OR'
    BUNGOMA = 'BU'
    KIKUYU = 'KU'
    MOMBASA = 'MS'
    MSAMBWENI = 'MW'
    NANYUKI = 'NU'
    NYALI = 'NL'
    NAIVASHA = 'NV'
    ELDORET = 'EL'
    NYAHURURU = 'NH'
    UKUNDA = 'UK'
    MALINDI = 'MA'
    NYANDARUA = 'ND'
    KINOO = 'KN'
    KILELESHWA = 'LE'
    RUIRU = 'RU'
    KABETE = 'KB'
    KAHAWAWEST = 'WS'
    MAVOKO = 'MK'
    KAKAMEGA = 'KK'
    MACHAKOS = 'MC'
    NYERI = 'NE'
    KIAMBU = 'KM'
    


    #Category Choices
    APARTMENTS = 'AP'
    LAND = 'LD'
    COWORKING = 'CO'
    HOMES = 'HO'
    OFFICES = 'OF'
    STUDIOS = 'ST'
    WAREHOUSES = 'WR'
    SHOPS = 'SH'



    AREA_CHOICES = {
        (WESTLANDS , 'Westlands'),
        (LIKONI , 'Likoni'),
        (KAHAWAWENDANI ,'Kahawa Wendani'),
        (NAROK ,'Narok'),
        (KILIMANI , 'Kilimani'),
        (NAKURU ,'Nakuru'),
        (DAGORETTI , 'Dagoretti'),
        (NYAMIRA ,'Nyamira'),
        (RUAKA ,'Ruaka'),
        (KAHAWASUKARI ,'Kahawa Sukari'),
        (KISERIAN , 'Kiserian'),
        (NAMANGA ,'Namanga'),
        (KISII ,'Kisii'),
        (LORESHO ,'Loresho'),
        (JUJA , 'Juja'),
        (KWALE , 'Kwale'),
        (WATAMU , 'Watamu'),
        (KITHIANI ,'Kithiani'),
        (LIMURU ,'Limuru'),
        (MVITA , 'Mvita'),
        (KAJIADO ,'Kajiado'),
        (KAREN ,'Karen'),
        (KITENGELA ,'Kitengela'),
        (LAVINGTON ,'Lavington'),
        (ATHIRIVER ,'Athi River'),
        (LANGATA ,'Langata'),
        (ISINYA , 'Isinya'),
        (KISAUNI , 'Kisauni'),
        (KILIFI ,'Kilifi'),
        (SYOKIMAU ,'Syokimau'),
        (ONGATARONGAI ,'Ongata Rongai'),
        (BUNGOMA ,'Bungoma'),
        (KIKUYU ,'Kikuyu'),
        (MOMBASA ,'Mombasa'),
        (MSAMBWENI ,'Msambweni'),
        (NANYUKI ,'Nyanyuki'),
        (NYALI , 'Nyali'),
        (NAIVASHA , 'Naivasha'),
        (ELDORET , 'Eldoret'),
        (NYAHURURU , 'Nyahururu'),
        (UKUNDA, 'Ukunda'),
        (MALINDI ,'Malindi'),
        (NYANDARUA, 'Nyandarua'),
        (KINOO ,'Kinoo'),
        (KILELESHWA ,'Kileleshwa'),
        (RUIRU ,'Ruiru'),
        (KABETE ,'Kabete'),
        (KAHAWAWEST ,'Kahawa West'),
        (MAVOKO ,'Mavoko'),
        (KAKAMEGA ,'Kakamega'),
        (MACHAKOS ,'Machakos'),
        (NYERI ,'Nyeri'),
        (KIAMBU ,'Kiambu'),
    } 

    CATEGORY_CHOICES = (
       (APARTMENTS, 'Apartments'),
       (LAND, 'Land'),
       (COWORKING, 'Coworking'),
       (HOMES, 'Homes'),
       (OFFICES, 'Offices'),
       (STUDIOS, 'Studios'),
       (WAREHOUSES, 'Warehouses'),
       (SHOPS, 'Shops'),
    )

    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    realtor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    area = models.CharField(max_length=2, choices=AREA_CHOICES)
    city = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, default = 0)
    billing = models.CharField(max_length=200, blank=True)
    minPrice = models.IntegerField(blank=True, default = 0)
    maxPrice = models.IntegerField(blank=True, default = 0)
    bedrooms = models.IntegerField(blank=True, default = 0)
    bathrooms = models.IntegerField(blank=True, default = 0)
    sqft = models.IntegerField(blank=True, default = 0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)
    list_date = models.DateTimeField('date created', blank=True, auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self): 
       return reverse("user-dashboard") 

    def save(self, *args, **kwargs): 
        if self.is_published and self.list_date is None:
            self.list_date = datetime.datetime.now()
        elif not self.is_published and self.list_date is not None:
            self.list_date = None
        super(Listing, self).save(*args, **kwargs)

    
    def get_time_diff(self):
        if self.list_date:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.list_date
            return math.floor(timediff.total_seconds()/86400)
    
    get_time_diff.short_description = 'Days Listed'






         
    # def get_absolute_url(self):
    #     return reverse('listing', kwargs={'pk': self.pk})