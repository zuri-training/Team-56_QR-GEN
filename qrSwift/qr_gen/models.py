from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Models for generating qr codes 

class WebsiteUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    website_url = models.URLField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)



class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)



class SendEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    to = models.EmailField()
    cc = models.CharField(max_length=1000)
    bcc = models.EmailField()
    subject = models.CharField(max_length=1000)
    body = models.TextField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)



class MeCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    nickname = models.CharField(max_length=200)
    birthday = models.DateField()
    url = models.URLField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    org = models.CharField(max_length=300)

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)




class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    twitter = models.URLField()
    linked_in = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)



class WifiConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ssid = models.CharField(max_length=100)
    authentication = models.CharField(max_length=250)
    password = models.CharField(max_length=400)
    hidden = models.BooleanField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)



class Coordinates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    latitude = models.FloatField()
    longitude = models.FloatField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)
