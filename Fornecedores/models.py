from django.db import models

class Fornecedor(models.Model):
    empresa = models.CharField(max_length= 50) 
    representante = models.CharField(max_length= 70)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length= 70)
    pais = models.CharField(max_length= 80)


