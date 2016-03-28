from django.db import models
from core.models import Ponto

# Create your models here.

class Pessoa(Ponto):
    pass

class Obra(Ponto, models.Model):
    pass

    @staticmethod
    def get_all():
        return Obra.objects.all()

    @staticmethod
    def get_obra_em_comunidade(pkComunidade):
        return Obra.objects.filter(comunidadeElemento_id=pkComunidade).order_by('id')

    @staticmethod
    def get_obra_em_categoria(pkCategoria):
        return Obra.objects.filter(listaTags__id=pkCategoria).order_by('id')

class Artista(Pessoa, models.Model):
    listaObras = models.ManyToManyField(Obra, blank = True)

    @staticmethod
    def get_all():
        return Artista.objects.all()

    @staticmethod
    def get_artista_em_comunidade(pkComunidade):
        return Artista.objects.filter(comunidadeElemento_id=pkComunidade).order_by('id')

    @staticmethod
    def get_artista_em_categoria(pkCategoria):
        return Artista.objects.filter(listaTags__id=pkCategoria).order_by('id')
