from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_usuario', views.user_register, name='user_register'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('listar_usuarios/', views.user_list, name='user_list'),
    path('editar_usuario/<int:id_user>', views.user_edit, name='user_edit'),
    path('editar_senha_usuario/<int:id_user>', views.user_edit_password, name='user_edit_password'),
    path('deletar_usuario/<int:id_user>', views.user_delete, name='user_delete')
]
