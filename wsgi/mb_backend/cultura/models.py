from django.db import models
from core.models import Elemento

# Create your models here.
class PontoTuristico(Elemento, models.Model):

    @staticmethod
    def get_all():
        return PontoTuristico.objects.all()

    @staticmethod
    def get_pontoturistico_em_comunidade(pkComunidade):
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def get_pontoturistico_em_categoria(pkCategoria):
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')

class Obra(Elemento, models.Model):
    pass

    @staticmethod
    def get_all():
        return Obra.objects.all()

    @staticmethod
    def get_obra_em_comunidade(pkComunidade):
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def get_obra_em_categoria(pkCategoria):
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')

class Artista(Elemento, models.Model):
    listaObras = models.ManyToManyField(Obra, blank = True)

    @staticmethod
    def get_all():
        return Artista.objects.all()

    @staticmethod
    def get_artista_em_comunidade(pkComunidade):
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def get_artista_em_categoria(pkCategoria):
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')
