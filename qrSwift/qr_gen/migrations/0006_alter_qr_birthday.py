# Generated by Django 4.0.6 on 2022-08-04 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0005_qr_birthday_qr_city_qr_country_qr_email_qr_nickname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
