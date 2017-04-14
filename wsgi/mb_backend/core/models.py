from django.db import models
from stdimage.models import StdImageField
from django.utils import timezone

# importacoes necessarias para a renomeacao das imagens
from django.utils.deconstruct import deconstructible
import os
from uuid import uuid4



# Create your models here.
class Bairro(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField(blank = True, null = True)
    longitude = models.FloatField(blank = True, null=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Bairro.objects.all().order_by('nome')

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Categoria.objects.all().order_by('nome')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

class EntidadeComunitaria(models.Model):
    bairro = models.ForeignKey(Bairro)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank = True)
    lista_de_categorias = models.ManyToManyField(Categoria, blank=True)
    path_and_rename = PathAndRename("None/")
    imagem = StdImageField(upload_to=path_and_rename,
        variations={
            'large': (1280, 720),
            'medium': (300, 200),
    })
    link_do_video = models.URLField(max_length=100, blank=True)

    class Meta:
        unique_together = ["bairro", "nome"]





class PontoReferencia(EntidadeComunitaria):
    latitude = models.FloatField(blank = True, null=True)
    longitude = models.FloatField(blank = True, null=True)
    endereco_oficial = models.CharField(max_length=500, blank = True)
    endereco_usual = models.CharField(max_length=500, blank=True)
