# Generated by Django 4.0.6 on 2022-08-04 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0004_alter_qr_qr_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 4)),
        ),
        migrations.AddField(
            model_name='qr',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='qr',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='qr',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='qr',
            name='nickname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='qr',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='qr',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='qr',
            name='name',
            field=models.CharField(default=datetime.date(2022, 8, 4), max_length=200),
        ),
    ]
