# Generated by Django 4.0.6 on 2022-08-04 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0004_alter_qr_qr_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='name',
            field=models.CharField(default=datetime.date(2022, 8, 4), max_length=200),
        ),
    ]
