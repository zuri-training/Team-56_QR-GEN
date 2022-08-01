from . import models
from rest_framework import serializers





class CreateText_QRSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextAndUrl
        fields = ("qr_name", "text", "generated_qr", "created_timestamp")


    def create(self, validated_data):
        
        qr_name = validated_data.get("qr_name")
        text = validated_data.get("text")
        generated_qr = validated_data.get("generated_qr")
        created_timestamp = validated_data.get("created_timestamp")
        


        text_qr = models.Text.objects.create(
          
           qr_name = qr_name,
           text= text,
           generated_qr = generated_qr,
           created_timestamp = created_timestamp,
        )

        return text_qr

