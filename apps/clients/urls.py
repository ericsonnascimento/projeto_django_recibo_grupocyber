from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_cliente/', views.client_register, name='client_register'),
    path('listar_clientes/', views.client_list, name='client_list'),
    path('editar_cliente/<int:id_client>', views.client_edit, name='client_edit'),
    path('deletar_cliente/<int:id_client>', views.client_delete, name='client_delete')
]
