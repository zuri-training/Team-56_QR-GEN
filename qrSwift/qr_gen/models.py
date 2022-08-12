from statistics import mode
import django
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from datetime import date
from .enums import QrType
from segno import helpers
from qr_code.qrcode import maker
from qr_code.qrcode.utils import QRCodeOptions
from django.core.files.base import ContentFile

import random

# Create your models here.
class Qr(models.Model):
    name = models.CharField(max_length=200, default=date.today())
    qr_code = models.ImageField(upload_to='qr_codes', blank=True) # Field To store qr_code field
    qr_type = models.CharField(max_length=12, choices=[(qr, qr.value) for qr in QrType], default=QrType.URL)
    content = models.CharField(max_length=200, blank=qr_type == QrType.WIFI)
    ## Fields for Wifi Configuration
    ssid = models.CharField(max_length=250, blank=True, default="")
    authentication = models.CharField(max_length=250, blank=True, default="")
    password = models.CharField(max_length=400, blank=True, default="")
    hidden = models.BooleanField(blank=True, default=False)
    ## Fields for my card
    firstname = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    birthday = models.DateField(blank=True, default=django.utils.timezone.now)
    url = models.URLField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    ## End Field for my card
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

    def qr_options(self):
        return QRCodeOptions(size="m", border=4, image_format="png")

    def generate_qr(self, qrcode_img):
        buff = maker.io.BytesIO()
        fname = f'qr_code-{self.name}-{self.created_at}' + '.png'
        qrcode_img.save(buff, kind="png")
        self.qr_code.save(fname, ContentFile(buff.getvalue()), save=False)

    def save(self,*args,**kwargs):
        
        if self.qr_type == "URL":
            qrcode_img=qrcode.make(self.content)
            canvas=Image.new("RGB", (300,300),"white")
            draw=ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.name}-{self.created_at}' + '.png'
            buffer=BytesIO()
            canvas.save(buffer,"PNG")
            self.qr_code.save(fname,File(buffer),save=False)
            canvas.close()
        elif self.qr_type == "WIFI" :
            wifi_info = helpers.make_wifi_data(ssid=self.ssid, password=self.password, security=self.authentication, hidden=self.hidden)
            qrcode_img = maker.make_qr(data=wifi_info, qr_code_options=self.qr_options(), force_text=False)
            buff = maker.io.BytesIO()
            fname = f'qr_code-{self.name}-{self.created_at}' + '.png'
            qrcode_img.save(buff, kind="png")
            self.qr_code.save(fname, ContentFile(buff.getvalue()), save=False)
        elif self.qr_type == "CARD":
            me_card_data = helpers.make_mecard_data(name=self.firstname, reading=None, email=self.email, phone=self.phone, videophone=None, memo=None, nickname=self.nickname, birthday=self.birthday, url=self.url, city=self.city, country=self.country)
            qrcode_img = maker.make_qr(data=me_card_data, qr_code_options=self.qr_options(), force_text=False)
            self.generate_qr(qrcode_img=qrcode_img)
        super().save(*args,**kwargs)