from django.db import models
from django.utils import timezone

# Create your models here.
class Comunidade(models.Model):
    nomeComunidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeComunidade

class Tag(models.Model):
    nomeTag = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeTag

class Elemento(models.Model):
    comunidadeElemento = models.ForeignKey(Comunidade)
    nome = models.CharField(max_length=100)
    enderecoOficial = models.CharField(max_length=500)
    enderecoUsual = models.CharField(max_length=500)
    descricao = models.TextField()
    listaTags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    localizacaoElemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.localizacaoElemento)


class Comentario(models.Model):
    elementoComentario = models.ForeignKey(Elemento)
    nomeUsuario = models.ForeignKey('auth.User')
    textoComentario = models.CharField(max_length=300)

    def __str__(self):
        return self.nomeUsuario

class PontoTuristico(Elemento, models.Model):
    pass

class Estabelecimento(Elemento):
    nomeProprietario = models.CharField(max_length=80)

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
    horaInicio = models.TimeField(auto_now=False, auto_now_add=False)
    horaFim = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.dia

class EstabelecimentoFixo(Estabelecimento, models.Model):
    listaDatas = models.ManyToManyField(Datas)

class EstabelecimentoMovel(Estabelecimento, models.Model):
    pass


class Agenda(models.Model):
    agendaMovel = models.ForeignKey(EstabelecimentoMovel)
    listaDatas = models.ManyToManyField(Datas)


class Evento(Elemento, models.Model):

    dataEvento = models.DateField(auto_now=False, auto_now_add=False)
    horaInicio = models.TimeField(auto_now=False, auto_now_add=False)
    horaFim = models.TimeField(auto_now=False, auto_now_add=False)

class Obra(models.Model):
    titulo = models.CharField(max_length=80)

    def __str__(self):
        return self.titulo

class Artista(Elemento, models.Model):
    listaObras = models.ManyToManyField(Obra)
