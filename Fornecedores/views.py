from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Fornecedores import views
from .models import Fornecedor
from django.contrib import messages
from django.contrib.auth.models import User




# Create your views here.
def index(request):
    lista_fornecedor = Fornecedor.objects.all()
    return render(request, 'fornecedor_index.html', {'lista': lista_fornecedor})


def cadastro(request):
    usuario = request.user

    if Fornecedor.objects.filter(representante=usuario).exists():
        return redirect('index')
    if usuario.is_authenticated:
        return render(request,'fornecedor_cadastro.html')
    else:
        return redirect('index')

def criar(request):
    if request.method == 'POST':
        empresa = request.POST.get('nomeempresa')
        telefone = request.POST.get('telefone')
        cnpj = request.POST.get('CNPJ')
        endereco = request.POST.get('endereco')
        pais = request.POST.get('pais')

        erros = {}
        error_text = 'Campo não preenchido!'

        if not empresa:
            erros['empresa'] = error_text
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
            return render(request, 'fornecedor_cadastro.html', {'erros': erros})

        # Cria o objeto Fornecedor associado ao usuário logado
        fornecedor = Fornecedor.objects.create(
            empresa=empresa,
            representante=request.user,  # Usuário logado
            telefone=telefone,
            cnpj=cnpj,
            endereco=endereco,
            pais=pais
        )

        return redirect('fornecedor_index')

    return render(request, 'fornecedor_cadastro.html')


  
   
    