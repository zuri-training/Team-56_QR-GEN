from django.urls import path
from . import views

urlpatterns = [
    path("create-qr/", views.create_qr),
    path("delete-qr/<int:id>", views.delete_qr)
]