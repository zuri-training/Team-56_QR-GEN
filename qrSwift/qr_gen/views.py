from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from qr_code.qrcode import maker


from rest_framework import status
# Create your views here.


@api_view(["POST"])
def create_text_qr(request):
    serializer = serializers.CreateText_QRSerializer(data= request.data)
    serializer.is_valid(raise_exception=True)

    
    text_qr = serializer.save()
    maker.make_qr( )

    return Response


















# @api_view(['POST'])
# def create_qr(request):

#     if not 'content' in request.data or not request.data["content"]:
#         return Response({"error": "Qr content is required"}, status=status.HTTP_400_BAD_REQUEST)
#     if not 'userId' in request.data:
#         return Response({"error": "userId is required"}, status=status.HTTP_400_BAD_REQUEST)
#     if not 'numberOfQrToGenerate' in request.data:
#         return Response({"error": "Number of Qr code to generated is required"}, status=status.HTTP_400_BAD_REQUEST)

#     # Generate the qr code with content

#     qr_content = request.data["content"]
#     user_id = request.data["userId"]
#     number_of_qr_to_generate = request.data['numberOfQrToGenerate']
#     return Response({"content": qr_content, "userId": user_id, "numberOfQrToGenerate":  number_of_qr_to_generate})
