from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length= 70) 
    distribuidor  = models.CharField(max_length= 70)
    preco = models.IntegerField()
    estoque = models.IntegerField(max_length= 70)
   

class Avaliacao(models.Model):
    comentario = models.CharField(max_length= 150)
    