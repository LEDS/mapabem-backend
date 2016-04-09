from rest_framework import serializers
from .models import Comercio
from core.serializers import ComunidadeSerializer, CategoriaSerializer


class ComercioSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    lista_de_categorias =CategoriaSerializer(many = True)

    class Meta:
        model = Comercio
        fields = ('id', 'comunidade', 'nome', 'nome_do_proprietario', 'telefone','endereco_oficial', 'endereco_usual', 'latitude', 'longitude', 'descricao', 'lista_de_categorias', 'imagem')


class ComercioSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Comercio
        fields = ('id', 'nome', 'descricao', 'imagem')
