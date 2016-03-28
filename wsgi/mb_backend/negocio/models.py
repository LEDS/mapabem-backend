from django.db import models
from django.utils import timezone
from core.models import ElementoFixo

# Create your models here.
class Comercio(ElementoFixo):
    nomeDoProprietario = models.CharField(max_length=80, blank = True)

    @staticmethod
    def get_all():
        return Comercio.objects.all()

    @staticmethod
    def get_comercio_em_comunidade(pkComunidade):
        return Comercio.objects.filter(comunidadePonto_id=pkComunidade).order_by('id')

    @staticmethod
    def get_comercio_em_categoria(pkCategoria):
        return Comercio.objects.filter(listaTags__id=pkCategoria).order_by('id')
