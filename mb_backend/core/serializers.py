from rest_framework import serializers
from .models import Comunidade, Elemento, Tag, EstabelecimentoFixo, Evento, Obra, Artista, Localizacao

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ('nomeComunidade',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('nomeTag',)

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ('latitude', 'longitude')


class ElementoSerializer(serializers.ModelSerializer):
    comunidadeElemento = ComunidadeSerializer()
    listaTags =TagSerializer(many = True)

    class Meta:
        model = Elemento
        fields = ('comunidadeElemento', 'nome', 'enderecoOficial', 'enderecoUsual', 'descricao', 'listaTags')