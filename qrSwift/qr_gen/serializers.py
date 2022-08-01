from . import models
from rest_framework import serializers





class CreateText_QRSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextAndUrl
        fields = ("user", "text", "generated_qr", "created_timestamp")


    def create(self, validated_data):
        user = validated_data.get("user")
        text = validated_data.get("text")
        generated_qr = validated_data.get("generated_qr")
        created_timestamp = validated_data.get("created_timestamp")
        


        text_qr = models.Text.objects.create(
           user = user,
           text= text,
           generated_qr = generated_qr,
           created_timestamp = created_timestamp,
        )

        return text_qr

