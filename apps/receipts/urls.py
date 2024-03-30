from django.urls import path
from . import views

urlpatterns = [
    path('recibos/', views.receipts, name='receipts'),
    path('dashboard/', views.index, name='index'),
]
