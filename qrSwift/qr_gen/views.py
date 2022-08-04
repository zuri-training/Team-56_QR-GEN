from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .models import Qr
from .serializers import  QrMeCardSerializers, QrSerializersText, QrWifiSerializers
import json
# Create your views here.


@api_view(['POST'])
def create_qr(request):

    if not 'userId' in request.data:
        return Response({"error": "userId is required"}, status=status.HTTP_400_BAD_REQUEST)
    # Generate the qr code with content

    if not 'qr_type' in request.data:
        return Response({"error": "qr_type is required"}, status=status.HTTP_400_BAD_REQUEST)
        
    qr_type = request.data["qr_type"]
    
    if qr_type == "CARD":
        serializer = QrMeCardSerializers(data=request.data)
        if serializer.is_valid():
            qr_code = serializer.save()
            json = QrMeCardSerializers(qr_code).data

            return Response({"res": "Qr code creared", "qr": json}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif qr_type == "WIFI":
        serializer = QrWifiSerializers(data=request.data)
        if serializer.is_valid():
            qr_code = serializer.save()
            json = QrWifiSerializers(qr_code).data

            return Response({"res": "Qr code  created", "qr": json}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif qr_type == "URL":
        serializer = QrSerializersText(data=request.data)
        if serializer.is_valid():
            qr_code = serializer.save()
            json = QrSerializersText(qr_code).data
            
            return Response({"res": "Qr code  created", "qr": json}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def delete_qr(request, id):
    
    try:
        qr = Qr.objects.get(id=id)
    except:
        return Response({"res":"Qr with this Id don't exist"}, status=status.HTTP_404_NOT_FOUND)
    result = Qr.objects.get(id=id)
    result.delete()
    return Response({"res": "Qr delete successfully"}, status=status.HTTP_200_OK)