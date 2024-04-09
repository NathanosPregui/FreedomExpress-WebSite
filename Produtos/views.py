from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from Produtos import views
from .models import Produto
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('pesquisar_produto')

def cadastro(request):
    return render(request,'produtos_cadastro.html')

def criar(request):
    nome = request.POST.get('nome')
    distribuidor  = request.POST.get('distribuidor ')
    preco= request.POST.get('preco')
    estoque = request.POST.get('estoque')

    erros = {}
    error_text = 'Campo não preenchido!'
    # Verifica se todos os campos foram preenchidos
    if not nome:
        erros['nome'] =  error_text 
    if not distribuidor :
        erros['distribuidor '] = error_text 
    if not preco:
        erros['preco'] = error_text 
    if not estoque:
        erros['estoque'] = error_text 

    if erros:
        for field, error in erros.items():
            messages.error(request, error)

    if erros:
        return render(request, 'produtos_cadastro.html',{'erros': erros})

    produtos = Produto.objects.create(
        nome = nome, 
        distribuidor = distribuidor , 
        preco = preco, 
        estoque = estoque 
    )
    produtos.save()
    
    return redirect('produtos_index')


def search(request):
    search = request.GET.get('search')
    page_size = 60
    if search:
        lista_produtos = Produto.objects.filter(nome__icontains=search)
    else:
        lista_produtos = Produto.objects.all()
    
    paginator = Paginator(lista_produtos, page_size)  
    page = request.GET.get('page')
    
    try:
        produtoslista = paginator.page(page)
    except PageNotAnInteger:
        produtoslista = paginator.page(1)
    except EmptyPage:
        produtoslista = paginator.page(paginator.num_pages)
    
    return render(request, 'produtos_index.html', {'lista': produtoslista, 'search': search})

