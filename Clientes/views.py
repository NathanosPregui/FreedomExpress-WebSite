from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Clientes import views
from .models import Usuario


def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    data_nascimento = request.POST['data_nascimento']
    email = request.POST['email']
    cpf = request.POST['cpf']
    senha = request.POST['senha']
    rua = request.POST['rua']
    complemento = request.POST['complemento']
    numero = request.POST['numero']
    cliente = Usuario.objects.create(nome=nome, sobrenome=sobrenome, data_nascimento=data_nascimento, email=email, cpf=cpf , senha=senha, rua=rua, complemento=complemento, numero=numero)
    cliente.save()
    return redirect('cliente_index')

def index(request):
    lista_clientes = Usuario.objects.all()
    return render(request, 'cliente_index.html', {'lista': lista_clientes})

def cadastro(request):
    return render(request,'cliente_cadastro.html')