from random import choices
from urllib import request
from rest_framework import serializers
from .models import Qr
from .enums import QrType

class QrSerializers(serializers.Serializer):
    qr_type = serializers.ChoiceField(choices=["URL", "WIFI"])
    content = serializers.CharField(max_length=200, required=False)
    ssid = serializers.CharField(max_length=200, required=False)
    authentication = serializers.ChoiceField(choices=["WPA", "WEP"], required=False)
    password = serializers.CharField(max_length=400, required=False)
    hidden = serializers.BooleanField(required=False)

    def validate(self, attrs):

        try:
            if attrs['qr_type'] == "URL" and not attrs["content"]:
                raise serializers.ValidationError("Content is required")
        except:
            raise serializers.ValidationError({"error":"Content is required"})
        
        try:
            if attrs['qr_type'] == "WIFI" and not attrs["ssid"]:
                raise serializers.ValidationError({"error": "SSID is required"})
        except:
            raise serializers.ValidationError({"error": "SSID is required"})

        try:
            if attrs['qr_type'] == "WIFI" and not attrs["authentication"]:
                raise serializers.ValidationError({"error": "Authentication is required"})
        except:
            raise serializers.ValidationError({"error": "Authentication is required"})

        try:
            if attrs['qr_type'] == "WIFI" and not attrs["password"]:
                raise serializers.ValidationError({"error": "Password is required"})
        except:
            raise serializers.ValidationError({"error": "Password is required"})

        # try:
        #     if attrs['qr_type'] == "WIFI" and not attrs["hidden"]:
        #         raise serializers.ValidationError({"error": "Hidden is required"})
        # except:
        #     raise serializers.ValidationError({"error": "Hidden is required"})

        return super().validate(attrs)


    def create(self, validated_data):
        return Qr.objects.create(**validated_data)