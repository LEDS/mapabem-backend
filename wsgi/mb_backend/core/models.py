from django.db import models
from django.utils import timezone


# Create your models here.
class Comunidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Comunidade.objects.all()

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Categoria.objects.all()

class Ponto(models.Model):
    comunidade = models.ForeignKey(Comunidade)
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
        return Ponto.objects.all()

    @staticmethod
    def get_ponto_em_comunidade(pkComunidade):
        return Ponto.objects.filter(comunidade_id=pkComunidade).order_by('nome')

    @staticmethod
    def get_ponto_em_categoria(pkCategoria):
        return Ponto.objects.filter(listaCategorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_ponto_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return Ponto.objects.filter(comunidade_id = pkComunidade, listaCategorias__id=pkCategoria).order_by('nome')


class ElementoFixo(Ponto):
    pass


class PontoReferencia(ElementoFixo):
    pass

class PontoReferenciaComercial(PontoReferencia):
    nomeDoProprietario = models.CharField(max_length=80, blank = True)

class PontoReferenciaCultural(PontoReferencia):
    pass
