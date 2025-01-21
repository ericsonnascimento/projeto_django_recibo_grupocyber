from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_recibos/', views.receipts_register, name='receipts_register'),
    path('listar_recibos/', views.receipts_list, name='receipts_list'),
    path('editar_recibos/<int:id_receipt>', views.receipts_edit, name='receipts_edit'),
    path('excluir_recibos/<int:id_receipt>', views.receipts_delete, name='receipts_delete'),
]
