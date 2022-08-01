from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models


from rest_framework import status
# Create your views here.


@api_view(["POST"])
def create_text_qr(request):

    if not "userId" in request.data:
        return Response({"error": "userId is required"}, status = status.HTTP_400_BAD_REQUEST)
        #Generate the qr code with inputs

        
    serializer = serializers.CreateText_QRSerializer(data= request.data)
    if serializer.is_valid():
        qr_code = serializer.save()
        data = serializers.CreateText_QRSerializer.objects.get(id=int(str(qr_code)))
        return Response({"message": "Qr code  created", "url": data.qr_code.url},
         status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






