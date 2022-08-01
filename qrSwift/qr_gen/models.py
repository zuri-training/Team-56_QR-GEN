from distutils.command.upload import upload
from re import M
from django.db import models
from django.contrib.auth.models import User
from qr_code.qrcode import maker
from qr_code.qrcode.utils import QRCodeOptions


# Create your models here.

#Models for generating qr codes 



class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    generated_qr = models.ImageField(upload_to='qr_codes', blank=True)
    created_timestamp =models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.id


    def save(self,*args,**kwargs):

        qrcode_img = maker.make_qr(data =self.text, qr_code_options= QRCodeOptions(size= "m", border=4, image_format="png"),force_text=True)
        fname = f'qr_code-{self.user}' + 'qr_code-{self.id}' + '.png'
       
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}' + '.png'
        buffer=BytesIO()
        canvas.save(buffer,"PNG")

        self.generated_qr.save(fname, qrcode_img, save= False)
        canvas.close()
        
        super().save(*args, **kwargs)

        

        # qrcode_img=qrcode.make(self.content)
        # canvas=Image.new("RGB", (300,300),"white")
        # draw=ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code-{self.name}' + '.png'
        # buffer=BytesIO()
        # canvas.save(buffer,"PNG")
        # self.qr_code.save(fname,File(buffer),save=False)
        # canvas.close()
        # super().save(*args,**kwargs)



class WebsiteUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    website_url = models.URLField()

    generated_qr = models.ImageField(upload_to='qr_codes', blank=True)
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




# class Qr(models.Model):
#     name = models.CharField(max_length=200, default=date.today())
#     content = models.CharField(max_length=200)
#     qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    
#     def __str__(self):
#         return str(self.id)

#     def save(self,*args,**kwargs):
#       qrcode_img=qrcode.make(self.content)
#       canvas=Image.new("RGB", (300,300),"white")
#       draw=ImageDraw.Draw(canvas)
#       canvas.paste(qrcode_img)
#       fname = f'qr_code-{self.name}' + '.png'
#       buffer=BytesIO()
#       canvas.save(buffer,"PNG")
#       self.qr_code.save(fname,File(buffer),save=False)
#       canvas.close()
#       super().save(*args,**kwargs)