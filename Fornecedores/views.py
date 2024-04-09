from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Fornecedores import views
from .models import Fornecedor
from django.contrib import messages




# Create your views here.
def index(request):
    lista_fornecedor = Fornecedor.objects.all()
    return render(request, 'fornecedor_index.html', {'lista': lista_fornecedor})


def cadastro(request):
    return render(request,'fornecedor_cadastro.html')

def criar(request):
    empresa = request.POST.get('nomeempresa')
    representante = request.POST.get('representante')
    telefone = request.POST.get('telefone')
    cnpj = request.POST.get('CNPJ')
    endereco = request.POST.get('endereco')
    pais = request.POST.get('pais')

    erros = {}
    error_text = 'Campo não preenchido!'
    # Verifica se todos os campos foram preenchidos
    if not empresa:
        erros['empresa'] =  error_text 
    if not representante:
        erros['representante'] = error_text 
    if not telefone:
        erros['telefone'] = error_text 
    if not cnpj:
        erros['cnpj'] = error_text 
    if not endereco:
        erros['endereco'] = error_text 
    if not pais:
        erros['pais'] = error_text 

    if erros:
        for field, error in erros.items():
            messages.error(request, error)

    if erros:
        return render(request, 'fornecedor_cadastro.html', {'erros': erros})

    fornecedores = Fornecedor.objects.create(
        empresa=empresa, 
        telefone=telefone, 
        cnpj=cnpj, 
        endereco=endereco, 
        pais=pais
    )
    fornecedores.save()

    return redirect('fornecedor_index')


  
   
    