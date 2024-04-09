from django.urls import path
from Clientes import views

urlpatterns = [
    path('',views.index, name='cliente_index'),
    path('cadastro',views.cadastro, name='cliente_cadastro'),
    path('criar/cliente', views.criar, name='criar_cliente')
]
