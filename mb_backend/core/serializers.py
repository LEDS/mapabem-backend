from rest_framework import serializers
from .models import Comunidade, Elemento, Tag, EstabelecimentoFixo, Evento, Obra, Artista, Localizacao

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ('id', 'nomeComunidade')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'nomeTag')

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ('id', 'latitude', 'longitude')


class ElementoSerializer(serializers.ModelSerializer):
    comunidadeElemento = ComunidadeSerializer()
    listaTags =TagSerializer(many = True)

    class Meta:
        model = Elemento
        fields = ('id', 'comunidadeElemento', 'nome', 'enderecoOficial', 'enderecoUsual', 'descricao', 'listaTags')
