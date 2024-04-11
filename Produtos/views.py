from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from Produtos import views
from .models import Produto,ProdutosImagens
from Clientes.models import Usuario
from Fornecedores.models import Fornecedor
from django.contrib import messages
from django.db.models import Count


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

        # Criar uma instância do Produto
        produto = Produto.objects.create(
            nome=nome,
            distribuidor=distribuidor,
            preco=preco,
            estoque=estoque
        )

        # Salvar as imagens no modelo ProdutosImagens
        for i in range(1, 11):  # Loop para os 10 slots de imagem
            imagem = request.FILES.get(f'image{i}')
            if imagem:
                ProdutosImagens.objects.create(
                    produto=produto,  # Passando o produto criado aqui
                    image=imagem
                )

        return redirect('pesquisar_produto')  # Redirecionar para a página de sucesso após o cadastro

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
        imagem = ProdutosImagens.objects.filter(produto=produto).first()
        produtos_com_imagens.append({'produto': produto, 'imagem': imagem})

    return render(request, 'produtos_index.html', {'lista': produtoslista, 'search': search, 'produtos_com_imagens': produtos_com_imagens})
    #Usar esse codigo se precisar de varias imagens
    ''' 
    imagens_produtos = ProdutosImagens.objects.all()

    produtos_com_imagens=[]
    for produto in produtoslista:
        imagem = get_images_for_product(produto.id, imagens_produtos)
        produtos_com_imagens.append({'produto': produto, 'imagem': imagem})'''    

def get_images_for_product(product_id, images_list):
    return [image for image in images_list if image.produto_id == product_id]

