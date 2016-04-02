from django.db import models
from core.models import EntidadeComunitaria, PontoReferencia

# Create your models here.

class Pessoa(EntidadeComunitaria):
    telefone = models.CharField(max_length = 20, blank = True)

class ObraExposta(PontoReferencia):

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return ObraExposta.objects.all()

    @staticmethod
    def get_por_id(id):
        return ObraExposta.objects.filter(id=id)

    @staticmethod
    def get_por_nome(nome):
        return ObraExposta.objects.filter(nome=nome)

    @staticmethod
    def get_obra_exposta_em_comunidade(pkComunidade):
        return ObraExposta.objects.filter(comunidade_id=pkComunidade).order_by('id')

    @staticmethod
    def get_obra_exposta_em_categoria(pkCategoria):
        return ObraExposta.objects.filter(lista_categorias__id=pkCategoria).order_by('id')


    @staticmethod
    def get_obra_exposta_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return ObraExposta.objects.filter(comunidade_id = pkComunidade, lista_categorias__id=pkCategoria).order_by('nome')

class Artista(Pessoa):
    lista_obras = models.ManyToManyField(ObraExposta, blank = True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Artista.objects.all()

    @staticmethod
    def get_por_id(id):
        return Artista.objects.filter(id=id)

    @staticmethod
    def get_por_nome(nome):
        return Artista.objects.filter(nome=nome)

    @staticmethod
    def get_artista_em_comunidade(pkComunidade):
        return Artista.objects.filter(comunidade_id=pkComunidade).order_by('nome')

    @staticmethod
    def get_artista_em_categoria(pkCategoria):
        return Artista.objects.filter(lista_categorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_artista_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return Artista.objects.filter(comunidade_id = pkComunidade, lista_categorias__id=pkCategoria).order_by('nome')


class PontoReferenciaCultural(PontoReferencia):

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return PontoReferenciaCultural.objects.all()

    @staticmethod
    def get_por_id(id):
        return PontoReferenciaCultural.objects.filter(id=id)

    @staticmethod
    def get_por_nome(nome):
        return PontoReferenciaCultural.objects.filter(nome=nome)

    @staticmethod
    def get_ponto_referencia_cultural_em_comunidade(pkComunidade):
        return PontoReferenciaCultural.objects.filter(comunidade_id=pkComunidade).order_by('nome')

    @staticmethod
    def get_ponto_referencia_cultural_em_categoria(pkCategoria):
        return PontoReferenciaCultural.objects.filter(lista_categorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_ponto_referencia_cultural_em_comunidade_em_categoria(pkComunidade, pkCategoria):
        return PontoReferenciaCultural.objects.filter(comunidade_id = pkComunidade, lista_categorias__id=pkCategoria).order_by('nome')
