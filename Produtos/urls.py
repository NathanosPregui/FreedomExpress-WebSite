from django.urls import path
from Produtos import views

urlpatterns = [
    path('',views.index, name='produtos_index'),
    path('cadastro',views.cadastro, name='produtos_cadastro'),
    path('criar/produto', views.criar, name='criar_produto'),
    path('pesquisar/produto', views.search, name='pesquisar_produto'),
    path('Produto404', views.produtonaoexsite, name='produto_naoachado'),
    path('ver/produto/<int:id_produto>', views.visualizar_produto, name='visualizar_produto'),
    path('editar/produto/<int:id_produto>', views.produto_editar, name='produto_editar'),
    path('atualizar',views.atualizar_produto, name='atualizar_produto'),
    path('deletar/<int:id_produto>',views.deletar_produto,name = 'deletar_produto'),
    path('meusprodutos', views.meus_produtos, name='meus_produtos'),


]

