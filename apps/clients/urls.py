from django.urls import path
from . import views

urlpatterns = [
    path('client_register/', views.client_register, name='client_register'),
]
