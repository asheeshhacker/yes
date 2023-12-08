from django.db import models

# Create your models here.
class data1(models.Model):
    name = models.CharField( max_length=10)
    status = models.CharField(max_length=16)
    roll1 = models.CharField(max_length=18)
    roll2 = models.CharField(max_length=18)
    roll3 = models.CharField(max_length=18)
    roll4 = models.CharField(max_length=18)
    roll5 = models.CharField(max_length=18)
    spodify = models.CharField(max_length=1000)
    instgram = models.CharField(max_length=1000)
    discord = models.CharField(max_length=1000)
    btc = models.CharField(max_length=300)
    pic = models.ImageField( upload_to='', height_field=None, width_field=None, max_length=None)

    


    

    