from django.urls import path
from Fornecedores import views

urlpatterns = [
    path('',views.index, name='fornecedor_index'),
    path('cadastro',views.cadastro, name='fornecedor_cadastro'),
    path('criar/fornecedor', views.criar, name='criar_fornecedor')
]

