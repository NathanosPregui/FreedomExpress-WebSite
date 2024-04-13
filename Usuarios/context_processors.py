from Clientes.models import PerfilImages,Usuario
from django.contrib.auth.models import User
from Fornecedores.models import Fornecedor



def perfil_image(request):
    # Identificar o usuário logado
    usuario = request.user

    # Inicializar a variável de imagem como None
    image_url = None

    if usuario.is_authenticated:
        try:
            # Consultar o banco de dados para encontrar a imagem associada ao usuário
            perfil_image = PerfilImages.objects.get(usuario=usuario)
            
            # Construir a URL da imagem
            image_url = perfil_image.image.url if perfil_image.image else None
        except PerfilImages.DoesNotExist:
            pass

    # Retornar a URL da imagem de perfil no dicionário
    return {'perfil_image_url': image_url}



def check(request):
    usuario = request.user
    fornecedor = None
    check = None
    userID = None

    if usuario.is_authenticated:
        fornecedor = Fornecedor.objects.filter(representante=usuario)
        userID = Usuario.objects.filter(id=request.user.id)  # Correção aqui
        if fornecedor.exists():
            check = fornecedor

    return {'fornecedorcheck': check, 'userid': userID}
