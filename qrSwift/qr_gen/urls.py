from django.urls import path
from . import views

urlpatterns = [
    path("text-qr/", views.create_text_qr)
]