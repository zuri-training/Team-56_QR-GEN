from django.urls import path
from . import views

urlpatterns = [
    path("qr/create/", views.create_qr)
]