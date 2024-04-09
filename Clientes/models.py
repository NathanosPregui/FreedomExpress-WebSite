from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    nome = models.CharField(max_length= 50) 
    sobrenome = models.CharField(max_length= 70)
    data_nascimento = models.DateTimeField()
    email = models.CharField(max_length= 70,unique=True)
    cpf = models.CharField(max_length= 15,unique=True)
    senha = models.CharField(max_length= 30)
    rua = models.CharField(max_length= 200)
    numero = models.IntegerField(max_length= 8)
    complemento = models.CharField(max_length= 80, null=True)

