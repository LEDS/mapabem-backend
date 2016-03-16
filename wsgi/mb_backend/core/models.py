from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Comunidade(models.Model):
    nomeComunidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeComunidade

    @staticmethod
    def get_all():
        return Comunidade.objects.all()

class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeCategoria

    @staticmethod
    def get_all():
        return Categoria.objects.all()

class Elemento(models.Model):
    comunidadeElemento = models.ForeignKey(Comunidade)
    nome = models.CharField(max_length=100)
    enderecoOficial = models.CharField(max_length=500, blank = True)
    enderecoUsual = models.CharField(max_length=500)
    telefone = models.CharField(max_length = 20, blank = True)
    descricao = models.TextField(blank = True)
    latitude = models.FloatField(blank = True)
    longitude = models.FloatField(blank = True)
    listaCategorias = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to=None, blank=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Elemento.objects.all()

    @staticmethod
    def get_elemento_em_comunidade(pkComunidade):
        return Elemento.objects.filter(comunidadeElemento_id=pkComunidade).order_by('nome')

    @staticmethod
    def get_elemento_em_categoria(pkCategoria):
        return Elemento.objects.filter(listaCategorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_elemento_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return Elemento.objects.filter(comunidadeElemento_id = pkComunidade, listaCategorias__id=pkCategoria).order_by('nome')


class Comentario(models.Model):
    elementoComentario = models.ForeignKey(Elemento)
    nomeUsuario = models.ForeignKey('auth.User')
    textoComentario = models.CharField(max_length=300)

    def __str__(self):
        return str(self.nomeUsuario)
