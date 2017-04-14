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
    def get_comercio_em_bairro(pkBairro):
        return Comercio.objects.filter(bairro_id=pkBairro).order_by('nome')

    @staticmethod
    def get_comercio_em_categoria(pkCategoria):
        return Comercio.objects.filter(lista_de_categorias__id=pkCategoria).order_by('nome')

    @staticmethod
    def get_comercio_em_bairro_em_categoria(pkBairro, pkCategoria):
        return Comercio.objects.filter(bairro_id = pkBairro, lista_de_categorias__id=pkCategoria).order_by('nome')

    class Meta:
        verbose_name = "Comercio"
        verbose_name_plural = "Comercios"
