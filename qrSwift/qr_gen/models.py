from django.db import models



# Create your models here.

class Text(models.Model):
    text = models.CharField(max_length=1000)



class Email(models.Model):
    to = ""
    cc = ""
    bcc = ""
    subject = ""
    body = ""



class Tel(models.Model):
    pass


class Mecard(models.Model):
    name = ""
    reading = ""
    email = ""
    phone = ""
    nickname = ""
    birthday = ""
    url = ""
    city = ""
    country = ""
    org = ""

class Youtube(models.Model):
    pass

class SocialMedia(models.Model):
    pass


class WifiConfig(models.Model):
    ssid = ""
    authentication = ""
    password = ""
    hidden = False



class QrCode(models.Model):
    user = ""
    qrId =""
    

    def QrInput():
        pass


    generated_qr = ""

    created_timestamp =""