import random
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
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    qr_type = models.CharField(max_length=12, choices=[(qr, qr.value) for qr in QrType], default=QrType.URL)
    content = models.CharField(max_length=200, blank=qr_type == QrType.WIFI)
    ssid = models.CharField(max_length=250, blank=qr_type == QrType.URL, default="")
    authentication = models.CharField(max_length=250, blank=qr_type == QrType.URL, default="")
    password = models.CharField(max_length=400, blank=qr_type == QrType.URL, default="")
    hidden = models.BooleanField(blank=qr_type == QrType.URL, default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.id)

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
        else:
            wifi_info = helpers.make_wifi_data(ssid=self.ssid, password=self.password, security=self.authentication, hidden=self.hidden)
            qrcode_img = maker.make_qr(data=wifi_info, qr_code_options=QRCodeOptions(size="m", border=4, image_format="png"), force_text=False)
            buff = maker.io.BytesIO()
            fname = f'qr_code-{self.name}-{self.created_at}' + '.png'
            qrcode_img.save(buff, kind="png")
            self.qr_code.save(fname, ContentFile(buff.getvalue()), save=False)
        super().save(*args,**kwargs)