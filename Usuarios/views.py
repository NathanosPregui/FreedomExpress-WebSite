from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from Clientes.models import Usuario,PerfilImages
from Produtos.models import Produto,ProdutosImagens


# Create your views here.


def index(request):
    categorias = ['Action-Figures','Cosplay','Roupas','Brinquedos', 'Maquiagem',  'Peças', 'Eletronicos', 'Livros', 'Moveis', 'Decoracao', 'Esportes']
    
    produtos_com_imagens_por_categoria = {}
    
    for categoria in categorias:
        produtos_categoria = Produto.objects.filter(categoria=categoria)
        produtos_com_imagens = []
        for produto in produtos_categoria:
            imagem = ProdutosImagens.objects.filter(produto=produto).order_by('slot').first()
            produtos_com_imagens.append({'produto': produto, 'imagem': imagem})
        produtos_com_imagens_por_categoria[categoria] = produtos_com_imagens

    return render(request, 'index.html', {'produtos_com_imagens_por_categoria': produtos_com_imagens_por_categoria})


def login_user(request):
    usuario = request.user
               
    if usuario.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            user = authenticate(request,email=email,password=senha)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirecionar para a página inicial após o login
        else:
            return render(request, 'login.html',{'error_message':'usuario inexistente'})
        return render(request, 'login.html',{'error_message':'usuario inexistente'})



def logout(request):
    auth_logout(request)
    return redirect('index')

    
