from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Qr
from .serializers import QrSerializers
import json
# Create your views here.


@api_view(['POST'])
def create_qr(request):

    if not 'userId' in request.data:
        return Response({"error": "userId is required"}, status=status.HTTP_400_BAD_REQUEST)
    # Generate the qr code with content
    
    serializer = QrSerializers(data=request.data)
    if serializer.is_valid():
        qr_code = serializer.save()
        data = Qr.objects.get(id=int(str(qr_code)))

        return Response({"res": "Qr code  created", "qr": {"id": data.id, "url": data.qr_code.url, "content": data.content, "name": data.name}}, status=status.HTTP_201_CREATED)
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