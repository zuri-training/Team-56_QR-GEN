
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# testing initial setup
def index(request):
    return HttpResponse("This is the home page!")

@api_view(['POST'])
def create_qr(request):

    if not 'content' in request.data or not request.data["content"]:
        return Response({"error": "Qr content is required"} , status=status.HTTP_400_BAD_REQUEST)
    if not 'userId' in request.data:
        return Response({"error": "userId is required"} , status=status.HTTP_400_BAD_REQUEST)

    # Generate the qr code with content

    qrContent = request.data["content"]
    userId = request.data["userId"]
    return Response({"content": qrContent, "userId": userId})