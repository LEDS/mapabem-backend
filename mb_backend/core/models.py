from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Comunidade(models.Model):
    comunidadeuuid = uuid.uuid4()
    nomeComunidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeComunidade

class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeCategoria

class Elemento(models.Model):
    elementouuid = uuid.uuid4()
    comunidadeElemento = models.ForeignKey(Comunidade)
    nome = models.CharField(max_length=100)
    nomeDoProprietario = models.CharField(max_length=80)
    enderecoOficial = models.CharField(max_length=500, blank = True)
    enderecoUsual = models.CharField(max_length=500)
    telefone = models.CharField(max_length = 20, blank = True, null = True)
    descricao = models.TextField(blank = True, null = True)
    latitude = models.FloatField(blank = True, null = True)
    longitude = models.FloatField(blank = True, null = True)
    listaCategorias = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
        return self.nome


class Comentario(models.Model):
    elementoComentario = models.ForeignKey(Elemento)
    nomeUsuario = models.ForeignKey('auth.User')
    textoComentario = models.CharField(max_length=300)

    def __str__(self):
        return str(self.nomeUsuario)
