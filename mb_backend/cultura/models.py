from django.db import models
from core.models import Elemento

# Create your models here.
class PontoTuristico(Elemento, models.Model):
    pass

class Obra(Elemento, models.Model):
    pass

class Artista(Elemento, models.Model):
    listaObras = models.ManyToManyField(Obra)
