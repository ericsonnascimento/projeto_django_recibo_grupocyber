from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_recibos/', views.receipts_register, name='receipts_register'),
    path('listar_recibos/', views.receipts_list, name='receipts_list'),
    path('dashboard/', views.index, name='index'),
]
