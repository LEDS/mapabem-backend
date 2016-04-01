from django.db import models
from core.models import PontoReferencia

# Create your models here.
class Comercio(PontoReferencia):
    telefone = models.CharField(max_length = 20, blank = True)
    nomeDoProprietario = models.CharField(max_length=80, blank = True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Comercio.objects.all()

    @staticmethod
    def get_comercio_em_comunidade(pkComunidade):
        return Comercio.objects.filter(comunidade_id=pkComunidade).order_by('nome')

    @staticmethod
    def get_comercio_em_categoria(pkCategoria):
        return Comercio.objects.filter(listaCategorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_comercio_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return Comercio.objects.filter(comunidade_id = pkComunidade, listaCategorias__id=pkCategoria).order_by('nome')
