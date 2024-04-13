from django.urls import path
from Clientes import views


urlpatterns = [
    path('',views.index, name='cliente_index'),
    path('cadastro',views.cadastro, name='cliente_cadastro'),
    path('perfil/cliente/<int:id_user>',views.perfil_usuario, name='perfil_usuario'),
    path('atualizar',views.atualizar_usuario, name='atualizar_usuario'),
]

