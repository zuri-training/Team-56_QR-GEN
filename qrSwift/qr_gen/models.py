import random
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from datetime import date
import random

# Create your models here.
class Qr(models.Model):
    name = models.CharField(max_length=200, default=date.today())
    content = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    
    def __str__(self):
        return str(self.id)

    def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.content)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      fname = f'qr_code-{self.name}' + '.png'
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.qr_code.save(fname,File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)