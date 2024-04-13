from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Clientes import views
from .models import Usuario
from .models import PerfilImages
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
import os




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
                    password=senha,
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

                return redirect('login')  # Redirecionar para a página de cadastro após o registro

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



def perfil_usuario(request, id_user):
    usuario = request.user
    if usuario.is_authenticated:       
        usuario = get_object_or_404(Usuario, id=id_user)
        try:
            imagemperfil = PerfilImages.objects.filter(usuario=usuario).first()
        except PerfilImages.DoesNotExist:
            imagemperfil = None
        return render(request, 'cliente_editar.html', {'usuario': usuario, 'imagemperfil': imagemperfil})
    return redirect('index')

def atualizar_usuario(request):
    id_usuario = request.POST.get('id')
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(pk=id_usuario)
        except ObjectDoesNotExist:
            # Se o usuário não existir, redirecione ou exiba uma mensagem de erro
            messages.error(request, 'O usuário com o ID especificado não foi encontrado.')
            return redirect(reverse('perfil_usuario', kwargs={'id_user': id_usuario}))

        usuario.nome = request.POST.get('nome')
        usuario.sobrenome = request.POST.get('sobrenome')
        usuario.data_nascimento = request.POST.get('data_nascimento')
        usuario.email = request.POST.get('email')
        usuario.cpf = request.POST.get('cpf')
        usuario.rua = request.POST.get('rua')
        usuario.numero = request.POST.get('numero')
        usuario.complemento = request.POST.get('complemento')
        confirmarsenha = request.POST.get('confirsenha')
        senha = request.POST.get('senha')
        perfilimage = request.FILES.get('perfilimage')

        if senha:
            senha_criptografada = make_password(senha)
            usuario.password = senha_criptografada

            if confirmarsenha == senha:
                usuario.save()
                atualizar_imagem_perfil(usuario, perfilimage)
                # Redirecionar para a página de perfil do usuário com o ID do usuário
                return redirect(reverse('perfil_usuario', kwargs={'id_user': id_usuario}))
            else:
                erros = {}
                erros['confirmarsenha'] = 'Senha diferente'

                if erros:
                    for field, error in erros.items():
                        messages.error(request, error)

        else:
            # Salvar a alteração do usuário no banco de dados
            usuario.save()
            atualizar_imagem_perfil(usuario, perfilimage)
            # Redirecionar para a página de perfil do usuário com o ID do usuário
            return redirect(reverse('perfil_usuario', kwargs={'id_user': id_usuario}))

        # Redirecionar de volta para a página de perfil do usuário com o ID do usuário
    return redirect(reverse('perfil_usuario', kwargs={'id_user': id_usuario}))



def atualizar_imagem_perfil(usuario, perfilimage):
    try:
        perfil_image_bd = PerfilImages.objects.get(usuario=usuario)
    except PerfilImages.DoesNotExist:
        perfil_image_bd = None

    if perfil_image_bd:
        # Se já existe uma imagem de perfil para o usuário, exclua-a
        perfil_image_bd.delete()

    # Crie uma nova entrada de imagem de perfil para o usuário, se houver uma nova imagem
    if perfilimage:
        PerfilImages.objects.create(usuario=usuario, image=perfilimage)