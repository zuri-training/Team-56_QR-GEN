from rest_framework import serializers
from .models import Qr

class QrSerializers(serializers.Serializer):
    content = serializers.CharField(max_length=200)
   

    def create(self, validated_data):
        return Qr.objects.create(**validated_data)