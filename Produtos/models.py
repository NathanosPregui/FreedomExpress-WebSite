from django.db import models
from Clientes.models import Usuario
from Fornecedores.models import Fornecedor


class Produto(models.Model):
    nome = models.CharField(max_length= 70) 
    distribuidor  = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='Usuario')
    preco = models.FloatField()
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=70)
    descricao = models.CharField(max_length=600,null=True,blank=True)
   




class Avaliacao(models.Model):
    Produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='Produto')
    comentario = models.CharField(max_length= 150)
    

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]  # obtém a extensão do arquivo
    filename = f'perfilimage.{ext}'  
    return 'products/{0}/{1}'.format(instance.produto.id, filename)



class ProdutosImagens(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    slot = models.IntegerField()
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return str(self.Produto)