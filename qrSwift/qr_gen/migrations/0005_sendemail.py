# Generated by Django 4.0.6 on 2022-07-30 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qr_gen', '0004_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.EmailField(max_length=254)),
                ('cc', models.CharField(max_length=1000)),
                ('bcc', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('generated_qr', models.ImageField(upload_to='')),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
