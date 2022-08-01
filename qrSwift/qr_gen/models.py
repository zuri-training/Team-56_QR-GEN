
from django.db import models
from django.contrib.auth.models import User
from qr_code.qrcode import maker
from qr_code.qrcode.utils import QRCodeOptions
from datetime import date
from segno import helpers

from django.core.files.base import ContentFile
from segno import QRCode


# Create your models here.

#Models for generating qr codes 


class TextAndUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=date.today())

    text = models.TextField()

    generated_qr = models.ImageField(upload_to='qr_codes', blank=True)
    created_timestamp =models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


    def save(self,*args,**kwargs):

        qrcode_img = maker.make_qr(data =self.text, qr_code_options= QRCodeOptions(size= "m", border=4, image_format="png"),force_text=False)
        
        buff = maker.io.BytesIO()

        fname = f'qr_code-{self.name}' + '.png'
       
        qrcode_img.save(buff, kind="png")
        

        self.generated_qr.save(fname, ContentFile(buff.getvalue()), save= False)
     
        
        super().save(*args, **kwargs)








class SendEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=date.today())
    to = models.EmailField()
    cc = models.CharField(max_length=1000)
    bcc = models.EmailField()
    subject = models.CharField(max_length=1000)
    body = models.TextField()

    generated_qr = models.ImageField(upload_to = 'qr_codes', blank=True)
    created_timestamp =models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return str(self.id)


    def save(self,*args,**kwargs):
        email_info = helpers.make_make_email_data(to= self.to, cc=self.cc, bcc= self.bcc, subject=self.subject, body=self.body)

        
        qrcode_img = maker.make_qr(data= email_info, qr_code_options= QRCodeOptions(size= "m", border=4, image_format="png"),force_text=False)
    

        buff = maker.io.BytesIO()

        fname = f'qr_code-{self.name}' + '.png'
       
        qrcode_img.save(buff, kind="png")
        

        self.generated_qr.save(fname, ContentFile(buff.getvalue()), save= False)
     
        
        super().save(*args, **kwargs)







class MeCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=date.today())
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    nickname = models.CharField(max_length=200)
    birthday = models.DateField()
    url = models.URLField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    generated_qr = models.ImageField(upload_to= 'qr_codes', blank = True)
    created_timestamp =models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


    def save(self,*args,**kwargs):

        me_card_data = helpers.make_mecard_data(name=self.name, reading=None, email=self.email, phone=self.phone, videophone=None, memo=None, nickname=self.nickname, birthday=self.birthday, url=self.url, city=self.city, country=self.country)

        qrcode_img = maker.make_qr(data =me_card_data, qr_code_options= QRCodeOptions(size= "m", border=4, image_format="png"),force_text=False)
        
        buff = maker.io.BytesIO()

        fname = f'qr_code-{self.name}' + '.png'
       
        qrcode_img.save(buff, kind="png")
        

        self.generated_qr.save(fname, ContentFile(buff.getvalue()), save= False)
     
        
        super().save(*args, **kwargs)






class WifiConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=date.today())
    ssid = models.CharField(max_length=100)
    authentication = models.CharField(max_length=250)
    password = models.CharField(max_length=400)
    hidden = models.BooleanField()

    generated_qr = models.ImageField(upload_to='qr_codes', blank=True)
    created_timestamp =models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


    def save(self,*args,**kwargs):
        wifi_info = helpers.make_wifi_data(ssid=self.ssid,password=self.password, security=self.authentication, hidden=self.hidden)

        
        qrcode_img = maker.make_qr(data= wifi_info, qr_code_options= QRCodeOptions(size= "m", border=4, image_format="png"),force_text=False)
    

        buff = maker.io.BytesIO()

        fname = f'qr_code-{self.name}' + '.png'
       
        qrcode_img.save(buff, kind="png")
        

        self.generated_qr.save(fname, ContentFile(buff.getvalue()), save= False)
     
        
        super().save(*args, **kwargs)



class Coordinates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=date.today())
    latitude = models.FloatField()
    longitude = models.FloatField()

    generated_qr = models.ImageField()
    created_timestamp =models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.id)


    def save(self,*args,**kwargs):
        location_info = helpers.make_geo_data(lat=self.latitude,lng=self.longitude)

        
        qrcode_img = maker.make_qr(data= location_info, qr_code_options= QRCodeOptions(size= "m", border=4, image_format="png"),force_text=False)
    

        buff = maker.io.BytesIO()

        fname = f'qr_code-{self.name}' + '.png'
       
        qrcode_img.save(buff, kind="png")
        

        self.generated_qr.save(fname, ContentFile(buff.getvalue()), save= False)
     
        
        super().save(*args, **kwargs)


