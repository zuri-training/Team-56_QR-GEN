# Generated by Django 4.0.6 on 2022-07-31 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='name',
            field=models.CharField(default=datetime.date(2022, 7, 31), max_length=200),
        ),
    ]
