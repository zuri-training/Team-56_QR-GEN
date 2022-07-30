from django.contrib import admin
from . import models


# Register your models here.

admin.site.register(models.WebsiteUrl)

admin.site.register(models.Text)

admin.site.register(models.SendEmail)

admin.site.register(models.MeCard)

admin.site.register(models.SocialMedia)

admin.site.register(models.WifiConfig)

admin.site.register(models.Coordinates)
