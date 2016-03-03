from rest_framework import serializers
from .models import Comunidade, Elemento, Categoria

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ('id','nomeComunidade')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nomeCategoria')


class ElementoSerializer(serializers.ModelSerializer):
    comunidadeElemento = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Elemento
        fields = ('comunidadeElemento', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')
