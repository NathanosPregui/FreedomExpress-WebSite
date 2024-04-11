from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Clientes import views
from .models import Usuario
from .models import PerfilImages
from django.contrib import messages


'''def criar(request):
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
'''



def cadastro(request):

    usuario = request.user
    if usuario.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            # Coletar dados do formulário
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            data_nascimento = request.POST.get('data_nascimento')
            email = request.POST.get('email')
            cpf = request.POST.get('cpf')
            senha = request.POST.get('senha')
            confirmarsenha = request.POST.get('confirsenha')
            rua = request.POST.get('rua')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            perfilimage = request.FILES.get('perfilimage')  # Certifique-se de que o campo de upload é um campo de arquivo

            # Criar um novo usuário
           
            # Verifica se todos os campos foram preenchidos
            if confirmarsenha == senha:
                novo_usuario = Usuario.objects.create_user(
                    email=email,
                    senha=senha,
                    nome=nome,
                    sobrenome=sobrenome,
                    data_nascimento=data_nascimento,
                    cpf=cpf,
                    rua=rua,
                    numero=numero,
                    complemento=complemento
                )

                # Criar uma nova instância de PerfilImages
                if perfilimage:  # Verifique se uma imagem foi fornecida
                    PerfilImages.objects.create(
                        usuario=novo_usuario,
                        image=perfilimage
                    )

                return redirect('cliente_index')  # Redirecionar para a página de cadastro após o registro

            else:      
                erros = {}                     
                erros['confirmarsenha'] =  'Senha diferente'

                if erros:
                    for field, error in erros.items():
                        messages.error(request, error)

                if erros:
                    return render(request, 'cliente_cadastro.html', {'erros': erros})

            
        return render(request, 'cliente_cadastro.html')

def index(request):
    lista_clientes = Usuario.objects.all()
    return render(request, 'cliente_index.html', {'lista': lista_clientes})

