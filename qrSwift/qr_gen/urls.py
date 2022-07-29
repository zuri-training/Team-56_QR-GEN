from django.urls import path
from . import views

urlpatterns = [
    path("create-qr/", views.create_qr)
]