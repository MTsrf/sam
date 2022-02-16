from distutils.command.upload import upload
from unicodedata import name
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')


class Banner(models.Model):
    img = models.ImageField(upload_to='pics')
    offer_word = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    btn = models.CharField(max_length=25)

class Offer(models.Model):
    img = models.ImageField(upload_to='pics')
    offer_word = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    btn = models.CharField(max_length=25) 

class Trandy(models.Model):
    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length=255)
    offer_amt = models.FloatField()
    amount = models.FloatField()
    offer = models.BooleanField(default=False)

class Arrived(models.Model):
    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length=255)
    offer_amt = models.FloatField()
    amount = models.FloatField()
    offer = models.BooleanField(default=False)

class Brand(models.Model):
    img = models.ImageField(upload_to ='pics')
# Create your models here.
