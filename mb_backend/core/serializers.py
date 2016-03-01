from rest_framework import serializers
from .models import Comunidade, Elemento, Categoria

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ('nomeComunidade',)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nomeCategoria',)


class ElementoSerializer(serializers.ModelSerializer):
    comunidadeElemento = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Elemento
        fields = ('uuid','comunidadeElemento', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')
