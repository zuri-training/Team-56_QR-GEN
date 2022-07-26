from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# testing initial setup
def index(request):
    return HttpResponse("This is the home page!")
