from django.urls import path
from Fornecedores import views

urlpatterns = [
    path('',views.index, name='fornecedor_index'),
    path('cadastro',views.cadastro, name='fornecedor_cadastro'),
    path('criar/fornecedor', views.criar, name='criar_fornecedor'),
    path('editar/forcenedor/<int:id_fornecedor>', views.fornecedor_editar, name='editar_fornecedor'),
    path('atualizar', views.atualizar_fornecedor, name='atualizar_fornecedor'),
]

