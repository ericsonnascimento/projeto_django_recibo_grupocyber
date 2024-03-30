from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_cliente/', views.client_register, name='client_register'),
]
