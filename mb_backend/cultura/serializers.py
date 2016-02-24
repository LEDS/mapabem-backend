from rest_framework import serializers
from .models import PontoTuristico, Obra, Artista
from core.serializers import ComunidadeSerializer, TagSerializer

class PontoTuristicoSerializer(serializers.ModelSerializer):
    comunidadeElemento = ComunidadeSerializer()
    listaTags =TagSerializer(many = True)

    class Meta:
        model = PontoTuristico
        fields = ('comunidadeElemento', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaTags')


class ObraSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaTags =TagSerializer(many = True)

    class Meta:
        model = Obra
        fields = ('comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaTags')

class ArtistaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaTags =TagSerializer(many = True)
    listaObras = ObraSerializer(many = True)

    class Meta:
        model = Artista
        fields = ('comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaObras', 'listaTags')
