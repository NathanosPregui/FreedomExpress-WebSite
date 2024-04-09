from django.urls import path
from Produtos import views

urlpatterns = [
    path('',views.index, name='produtos_index'),
    path('cadastro',views.cadastro, name='produtos_cadastro'),
    path('criar/produto', views.criar, name='criar_produto'),
    path('pesquisar/produto', views.search, name='pesquisar_produto')
]

