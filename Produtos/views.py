from django.shortcuts import render,redirect, get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Produto,ProdutosImagens
from Clientes.models import Usuario
from Fornecedores.models import Fornecedor
from datetime import datetime, timedelta
from django.http import Http404
import locale
import os
from django.conf import settings
from django.urls import reverse









# Create your views here.

def index(request):
    return redirect('pesquisar_produto')

def cadastro(request):
    user = request.user  # Obtém o usuário logado

    if Fornecedor.objects.filter(representante=user).exists():
        return render(request,'produtos_cadastro.html')
    return redirect('index')

def criar(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        usuario_logado = request.user  # Obtém o usuário logado
        distribuidor = Usuario.objects.get(id=usuario_logado.id)  # Busca o fornecedor correspondente ao usuário logado
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('cateroria')


        precoformatado = float(substituir_virgula_por_ponto(str(preco)))
        if not categoria:
            return render(request, 'produtos_cadastro.html')
        # Criar uma instância do Produto
        produto = Produto.objects.create(
            nome=nome,
            distribuidor=distribuidor,
            preco=precoformatado,
            estoque=estoque,
            descricao= descricao,
            categoria=categoria
        )

        # Salvar as imagens no modelo ProdutosImagens
        for i in range(1, 11):  # Loop para os 10 slots de imagem
            imagem = request.FILES.get(f'image{i}')
            slotsave = i
            if imagem:
                ProdutosImagens.objects.create(
                    produto=produto,  # Passando o produto criado aqui
                    image=imagem,
                    slot = slotsave
                )

        return redirect(reverse('visualizar_produto', kwargs={'id_produto': produto}))

    else:
        # Se for uma requisição GET, renderize o template do formulário
        return render(request, 'produtos_cadastro.html')



def search(request):
    search = request.GET.get('search')
    page_size = 60
    if search:
        lista_produtos = Produto.objects.filter(nome__icontains=search).order_by('-id')
    else:
        lista_produtos = Produto.objects.all().order_by('-id')
    
    paginator = Paginator(lista_produtos, page_size)  
    page = request.GET.get('page')
    
    try:
        produtoslista = paginator.page(page)
    except PageNotAnInteger:
        produtoslista = paginator.page(1)
    except EmptyPage:
        produtoslista = paginator.page(paginator.num_pages)

    produtos_com_imagens = []
    for produto in produtoslista:
        imagem = ProdutosImagens.objects.filter(produto=produto).order_by('slot').first()
        produtos_com_imagens.append({'produto': produto, 'imagem': imagem})

    return render(request, 'produtos_index.html', {'lista': produtoslista, 'search': search, 'produtos_com_imagens': produtos_com_imagens})



def visualizar_produto(request, id_produto):
    search = request.GET.get('search')
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

        produto = get_object_or_404(Produto, pk=id_produto)
        data = (datetime.now() + timedelta(days=10)).day
        datacalculo = (datetime.now() + timedelta(days=20)).day
        datacalculomes = (datetime.now() + timedelta(days=20)).strftime("%B")
        imagens_produtos = ProdutosImagens.objects.filter(produto=produto).order_by('slot')

        recomendados = Produto.objects.filter(categoria = produto.categoria).exclude(pk=id_produto)[:3]


        usuario_fornecedor = None
        usuario_fornecedor_veficar = Fornecedor.objects.filter(representante=request.user)
        produtoproprietario = None  
        if usuario_fornecedor_veficar:
            if request.user.is_authenticated:
                usuario_fornecedor = get_object_or_404(Fornecedor, representante=request.user)

            if usuario_fornecedor:
                produtoproprietario = Produto.objects.filter(distribuidor=usuario_fornecedor)
            else:
                produtoproprietario = None  
       

        produtos_com_imagens = []
        for produtoitem in recomendados:
            imagem = ProdutosImagens.objects.filter(produto=produtoitem).first()
            produtos_com_imagens.append({'produto': produtoitem, 'imagem': imagem})

    except Http404:
        return redirect('produto_naoachado')

    return render(request, 'produtos_pagina.html', {'produto': produto, 'imagens_produtos': imagens_produtos, 'data': data, 'datadepois': f"{datacalculo} de {datacalculomes}",'recomendados':recomendados,'produtos_com_imagens': produtos_com_imagens,'proprietario' : produtoproprietario,'search':search})


def produtonaoexsite(request):
    return render(request,'produtos_naoexiste.html')

def substituir_virgula_por_ponto(texto):
    return texto.replace(',', '.')


def produto_editar(request,id_produto):
    try:
        produto = get_object_or_404(Produto, pk= id_produto)
        imagens_produtos = ProdutosImagens.objects.filter(produto=produto).order_by('slot')
        
        imagemslot = [] 
        for i in range(1, 11):
            if i not in [imagem.slot for imagem in imagens_produtos]:
                # Adiciona o slot vazio à lista slots_vazios
                imagemslot.append(i)       

    except Http404:
        return redirect('produto_naoachado')
    

    return render(request,'produtos_editar.html',{'produto':produto,'imagens_produtos':imagens_produtos,'slot':imagemslot})
    

def atualizar_produto(request):
    if request.method == "POST":
        id_produto = request.POST.get('id')
        produtosalvar = Produto.objects.get(pk=id_produto)
        produtosalvar.nome = request.POST.get('nome')
        precoformatado = float(substituir_virgula_por_ponto(str(request.POST.get('preco'))))
        produtosalvar.preco =  precoformatado 
        produtosalvar.estoque = request.POST.get('estoque')
        produtosalvar. descricao = request.POST.get('descricao')
        produtosalvar.descricao = request.POST.get('descricao')
        produtosalvar.categoria = request.POST.get('cateroria')

        

        # Salvar as imagens no modelo ProdutosImagens
        imagens = [request.FILES.get(f'image{i}') for i in range(1, 11)]
        atualizar_imagens_produto(produtosalvar, imagens)

        produtosalvar.save()
        return redirect(reverse('visualizar_produto', kwargs={'id_produto': id_produto}))

    else:
        # Se for uma requisição GET, renderize o template do formulário
        return render(request, 'produtos_cadastro.html')
    

def atualizar_imagens_produto(produto, imagens):
    for imagem in produto.produtosimagens_set.all():
        # Verificar se há uma imagem correspondente enviada pelo formulário
        slot = imagem.slot - 1  # Ajuste do slot para começar do índice 0
        nova_imagem = imagens[slot] if slot < len(imagens) else None
        if nova_imagem:
            # Se houver uma nova imagem para esse slot, substituir a imagem antiga
            # Primeiro, excluir a imagem antiga do banco de dados
            imagem.delete()
            # Em seguida, excluir o arquivo correspondente no sistema de arquivos, se existir
            if os.path.exists(imagem.image.path):
                os.remove(imagem.image.path)
            else:
                # Se o arquivo não existir, apenas exclua a entrada do banco de dados
                imagem.delete()
    # Salvar as novas imagens
    for i, imagem_file in enumerate(imagens, start=1):
        if imagem_file:
            ProdutosImagens.objects.create(
                produto=produto,
                image=imagem_file,
                slot=i
            )


def excluir_imagens_produto(produto):
    # Construir o caminho da pasta correspondente ao ID do produto
    pasta_produto = os.path.join('media', 'products', str(produto.id))

    # Verificar se a pasta do produto existe
    if os.path.exists(pasta_produto):
        # Excluir todos os arquivos na pasta
        for filename in os.listdir(pasta_produto):
            file_path = os.path.join(pasta_produto, filename)
            os.remove(file_path)
        # Excluir a pasta do produto
        os.rmdir(pasta_produto)

    # Excluir todas as entradas da tabela ProdutosImagens relacionadas ao produto
    produto.produtosimagens_set.all().delete()


def deletar_produto(request,id_produto):
    produto = get_object_or_404(Produto, pk = id_produto)
    

    excluir_imagens_produto(produto)


    produto.delete()
    return redirect('pesquisar_produto')



def meus_produtos(request):
    user = request.user
    fornecedor = Fornecedor.objects.get(representante=user)

    lista_produtos = Produto.objects.filter(distribuidor=fornecedor).order_by('-id')

    produtos_com_imagens = []
    for produto in lista_produtos:
        imagem = ProdutosImagens.objects.filter(produto=produto).order_by('slot').first()
        produtos_com_imagens.append({'produto': produto, 'imagem': imagem})
    return render(request, 'produtos_meusprodutos.html', {'lista_produtos': lista_produtos,'produtos_com_imagens': produtos_com_imagens})

