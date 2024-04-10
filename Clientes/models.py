from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import os



'''class Usuario(models.Model):
    nome = models.CharField(max_length= 50) 
    sobrenome = models.CharField(max_length= 70)
    data_nascimento = models.DateTimeField()
    email = models.CharField(max_length= 70,unique=True)
    cpf = models.CharField(max_length= 15,unique=True)
    senha = models.CharField(max_length= 30)
    rua = models.CharField(max_length= 200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length= 80, null=True)'''



class UsuarioManager(BaseUserManager):
    def create_user(self, email=None, senha=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self.create_user(email, senha, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=15, unique=True)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=80, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'cpf', 'data_nascimento','rua','numero']

    def get_full_name(self):
        return self.nome
    def get_short_name(self):
        return self.nome or self.email.split('@')[0]
    def __str__(self):
        return self.email
    
    
def user_directory_path(instance, filename):
    # Arquivo será carregado para MEDIA_ROOT/static/images/users/perfilusers/<id_do_usuario>/<filename>
    ext = filename.split('.')[-1]  # obtém a extensão do arquivo
    filename = f'perfilimage.{ext}'  
    return 'perfilusers/{0}/{1}'.format(instance.usuario.id, filename)


class PerfilImages(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='imagensperfil')
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return str(self.usuario)
