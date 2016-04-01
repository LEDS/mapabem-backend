from django.db import models
from django.utils import timezone


# Create your models here.
class Comunidade(models.Model):
    nome = models.CharField(max_length=50)
    latitude = models.FloatField(blank = True, null = True)
    longitude = models.FloatField(blank = True, null=True)

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

class EntidadeComunitaria(models.Model):
    comunidade = models.ForeignKey(Comunidade)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank = True)
    listaCategorias = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to=None, blank=True)



class PontoReferencia(EntidadeComunitaria):
    latitude = models.FloatField(blank = True, null=True)
    longitude = models.FloatField(blank = True, null=True)
    enderecoOficial = models.CharField(max_length=500, blank = True)
    enderecoUsual = models.CharField(max_length=500)
