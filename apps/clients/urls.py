from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_cliente/', views.client_register, name='client_register'),
    path('listar_clientes/', views.client_list, name='client_list'),
]
