from django.db import models
from core.models import PontoReferencia

# Create your models here.
class Comercio(PontoReferencia):
    telefone = models.CharField(max_length = 20, blank = True)
    nome_do_proprietario = models.CharField(max_length=80, blank = True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Comercio.objects.all()


    @staticmethod
    def get_por_id(id):
        return Comercio.objects.filter(id=id)

    @staticmethod
    def get_por_nome(nome):
        return Comercio.objects.filter(nome=nome)

    @staticmethod
    def get_comercio_em_comunidade(pkComunidade):
        return Comercio.objects.filter(comunidade_id=pkComunidade).order_by('nome')

    @staticmethod
    def get_comercio_em_categoria(pkCategoria):
        return Comercio.objects.filter(lista_categorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_comercio_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return Comercio.objects.filter(comunidade_id = pkComunidade, lista_categorias__id=pkCategoria).order_by('nome')
