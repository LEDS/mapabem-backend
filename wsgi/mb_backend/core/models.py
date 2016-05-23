from django.db import models
from stdimage.models import StdImageField
from django.utils import timezone

# importacoes necessarias para a renomeacao das imagens
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

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_all():
        return Categoria.objects.all().order_by('nome')

class EntidadeComunitaria(models.Model):
    # para se evitar erro ao inserir imagens com acentuacao foi utilizada esse metodo
    # o mesmo renomeia a imagem de acordo com uma uuid ou de acordo com a pk do objeto
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(instance.pk, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper


    bairro = models.ForeignKey(Bairro)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank = True)
    lista_de_categorias = models.ManyToManyField(Categoria, blank=True)
    imagem = StdImageField(upload_to=path_and_rename('None/'),
        variations={
            'large': (1280, 720),
            'medium': (300, 200),
    })

    class Meta:
        unique_together = ["bairro", "nome"]



class PontoReferencia(EntidadeComunitaria):
    latitude = models.FloatField(blank = True, null=True)
    longitude = models.FloatField(blank = True, null=True)
    endereco_oficial = models.CharField(max_length=500, blank = True)
    endereco_usual = models.CharField(max_length=500, blank=True)
