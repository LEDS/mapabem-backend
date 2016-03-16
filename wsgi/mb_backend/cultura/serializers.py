from rest_framework import serializers
from .models import PontoTuristico, Obra, Artista
from core.serializers import ComunidadeSerializer, CategoriaSerializer

class PontoTuristicoSerializer(serializers.ModelSerializer):
    comunidadeElemento = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = PontoTuristico
        fields = ('comunidadeElemento', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias')


class ObraSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Obra
        fields = ('comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias')

class ArtistaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)
    listaObras = ObraSerializer(many = True)

    class Meta:
        model = Artista
        fields = ('comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaObras', 'listaCategorias')
