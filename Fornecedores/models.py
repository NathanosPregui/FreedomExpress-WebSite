from django.db import models
from django.core.exceptions import ValidationError
from Clientes.models import Usuario

class Fornecedor(models.Model):
    empresa = models.CharField(max_length=50)
    representante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='representantes')
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=70)
    pais = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=14)


