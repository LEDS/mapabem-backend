from rest_framework import serializers
from .models import EstabelecimentoFixo, Evento, Datas
from core.serializers import ComunidadeSerializer, TagSerializer

class DatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datas
        fields = ('dia', 'horarioAbertura', 'horarioFechamento')

class EstabelecimentoFixoSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaTags =TagSerializer(many = True)

    class Meta:
        model = EstabelecimentoFixo
        fields = ('comunidade', 'nome', 'nomeProprietario', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaTags')


class EventoSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaTags = TagSerializer(many = True)
    listaDatas = DatasSerializer

    class Meta:
        model = Evento
        fields = ('comunidade', 'nome', 'dataEvento', 'horaInicio', 'horaFim', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaTags', 'listaDatas')
