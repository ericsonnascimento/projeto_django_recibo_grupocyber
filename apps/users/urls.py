from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_acesso', views.cadastro_acesso, name='cadastro_acesso'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('listar_usuarios/', views.user_list, name='user_list')
]
