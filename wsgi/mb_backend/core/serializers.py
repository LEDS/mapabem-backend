from rest_framework import serializers
from .models import Comunidade, EntidadeComunitaria, Categoria

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ('id','nome')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nome')


class EntidadeComunitariaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = EntidadeComunitaria
        fields = ('id', 'comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')
