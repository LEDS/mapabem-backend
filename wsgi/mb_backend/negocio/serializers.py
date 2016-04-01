from rest_framework import serializers
from .models import Comercio
from core.serializers import ComunidadeSerializer, CategoriaSerializer


class ComercioSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Comercio
        fields = ('id', 'comunidade', 'nome', 'nomeDoProprietario', 'telefone','enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')


class ComercioSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Comercio
        fields = ('id', 'nome', 'descricao', 'imagem')
