from django.db import models
from django.utils import timezone
from core.models import Elemento

# Create your models here.
class Estabelecimento(Elemento):
    nomeDoProprietario = models.CharField(max_length=80)

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
    def get_all():
        return EstabelecimentoFixo.objects.all()

    @staticmethod
    def get_estabelecimentofixo_em_comunidade(pkComunidade):
        return EstabelecimentoFixo.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def get_estabelecimentofixo_em_categoria(pkCategoria):
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
    def get_all():
        return Evento.objects.all()

    @staticmethod
    def get_evento_em_comunidade(pkComunidade):
        return Evento.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

    @staticmethod
    def get_evento_em_categoria(pkCategoria):
        return Evento.objects.filter(listaTags__id=tag).order_by('id')
