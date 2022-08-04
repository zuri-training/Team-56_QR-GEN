from random import choices
from urllib import request
from rest_framework import serializers
from .models import Qr
from .enums import QrType

class QrSerializersText(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=False)
    qr_type = serializers.ChoiceField(choices=["URL", "WIFI", "CARD"])
    content = serializers.CharField(max_length=200, required=False)
    id = serializers.IntegerField(required=False)
    qr_code = serializers.ImageField(required=False)

    def create(self, validated_data):
        return Qr.objects.create(**validated_data)


class QrWifiSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=False)
    id = serializers.IntegerField(required=False)
    qr_type = serializers.ChoiceField(choices=["URL", "WIFI", "CARD"])
    qr_code = serializers.ImageField(required=False)
    ssid = serializers.CharField(max_length=200, required=False)
    authentication = serializers.ChoiceField(choices=["WPA", "WEP"], required=False)
    password = serializers.CharField(max_length=400, required=False)
    hidden = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Qr.objects.create(**validated_data)


class QrMeCardSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=False)
    id = serializers.IntegerField(required=False)
    qr_type = serializers.ChoiceField(choices=["URL", "WIFI", "CARD"])
    qr_code = serializers.ImageField(required=False)
    firstname = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=100)
    nickname = serializers.CharField(max_length=200)
    birthday = serializers.DateField()
    url = serializers.URLField()
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Qr.objects.create(**validated_data)

