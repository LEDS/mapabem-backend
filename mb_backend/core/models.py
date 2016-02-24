from django.db import models
from django.utils import timezone

# Create your models here.
class Comunidade(models.Model):
    nomeComunidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeComunidade

class Tag(models.Model):
    nomeTag = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeTag

class Elemento(models.Model):
    comunidadeElemento = models.ForeignKey(Comunidade)
    nome = models.CharField(max_length=100)
    enderecoOficial = models.CharField(max_length=500)
    enderecoUsual = models.CharField(max_length=500)
    descricao = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    listaTags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nome


class Comentario(models.Model):
    elementoComentario = models.ForeignKey(Elemento)
    nomeUsuario = models.ForeignKey('auth.User')
    textoComentario = models.CharField(max_length=300)

    def __str__(self):
        return str(self.nomeUsuario)
