from django.db import models
from django.utils import timezone
from core.models import Elemento

# Create your models here.
class Estabelecimento(Elemento):
    pass

class Datas(models.Model):
    SEGUNDA_FEIRA = 'SEG'
    TERÇA_FEIRA = 'TER'
    QUARTA_FEIRA = 'QUA'
    QUINTA_FEIRA = 'QUI'
    SEXTA_FEIRA = 'SEX'
    SABADO = 'SAB'
    DOMINGO = 'DOM'

    DIAS_DA_SEMANA = (
    (SEGUNDA_FEIRA, 'Segunda-Feira'),
    (TERÇA_FEIRA, 'Terça-Feira'),
    (QUARTA_FEIRA, 'Quarta-Feira'),
    (QUINTA_FEIRA, 'Quinta-Feira'),
    (SEXTA_FEIRA, 'Sexta-Feira'),
    (SABADO, 'Sábado'),
    (DOMINGO, 'Domingo')
    )

    dia = models.CharField(max_length = 3, choices=DIAS_DA_SEMANA)
    horarioAbertura = models.TimeField(auto_now=False, auto_now_add=False)
    horarioFechamento = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.dia

class EstabelecimentoFixo(Estabelecimento, models.Model):
    listaDatas = models.ManyToManyField(Datas, blank = True)

    @staticmethod
    def getAll():
        return EstabelecimentoFixo.objects.all()

    @staticmethod
    def getEstabelecimentoFixoInComunidade(pkComunidade):
        return EstabelecimentoFixo.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def getEstabelecimentoFixoInCategoria(pkCategoria):
        return EstabelecimentoFixo.objects.filter(listaTags__id=tag).order_by('id')

class EstabelecimentoMovel(Estabelecimento, models.Model):
    pass


class Agenda(models.Model):
    agendaMovel = models.ForeignKey(EstabelecimentoMovel)
    listaDatas = models.ManyToManyField(Datas)


class Evento(Elemento, models.Model):

    dataEvento = models.DateField(auto_now=False, auto_now_add=False)
    horaInicio = models.TimeField(auto_now=False, auto_now_add=False)
    horaFim = models.TimeField(auto_now=False, auto_now_add=False)

    @staticmethod
    def getAll():
        return Evento.objects.all()

    @staticmethod
    def getEventoInComunidade(pkComunidade):
        return Evento.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def getPEventoInCategoria(pkCategoria):
        return Evento.objects.filter(listaTags__id=tag).order_by('id')
