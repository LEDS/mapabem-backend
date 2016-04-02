from django.db import models
from django.utils import timezone


# Create your models here.
class Comunidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField(blank = True, null = True)
    longitude = models.FloatField(blank = True, null=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Comunidade.objects.all()

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Categoria.objects.all()

class EntidadeComunitaria(models.Model):
    comunidade = models.ForeignKey(Comunidade)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank = True)
    lista_categorias = models.ManyToManyField(Categoria, blank=True)
    imagem = models.ImageField(upload_to=None, blank=True)

    class Meta:
        unique_together = ["comunidade", "nome"]



class PontoReferencia(EntidadeComunitaria):
    latitude = models.FloatField(blank = True, null=True)
    longitude = models.FloatField(blank = True, null=True)
    endereco_oficial = models.CharField(max_length=500, blank = True)
    endereco_usual = models.CharField(max_length=500, blank=True)
