# configure urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-qr/", views.create_qr)
    # path("main/", views.main, name="main"),
]
