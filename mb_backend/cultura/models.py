from django.db import models
from core.models import Elemento

# Create your models here.
class PontoTuristico(Elemento, models.Model):

    @staticmethod
    def getAll():
        return PontoTuristico.objects.all()

    @staticmethod
    def getPontoTuristicoInComunidade(pkComunidade):
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def getPontoTuristicoInCategoria(pkCategoria):
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')

class Obra(Elemento, models.Model):
    pass

    @staticmethod
    def getAll():
        return Obra.objects.all()

    @staticmethod
    def getObraInComunidade(pkComunidade):
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def getObraInCategoria(pkCategoria):
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')

class Artista(Elemento, models.Model):
    listaObras = models.ManyToManyField(Obra, blank = True)

    @staticmethod
    def getAll():
        return Artista.objects.all()

    @staticmethod
    def getArtistaInComunidade(pkComunidade):
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def getArtistaInCategoria(pkCategoria):
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')
