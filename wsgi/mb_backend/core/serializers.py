from rest_framework import serializers
from .models import Bairro, EntidadeComunitaria, Categoria

class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = ('id','nome')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nome')


class EntidadeComunitariaSerializer(serializers.ModelSerializer):
    bairro = BairroSerializer()
    lista_de_categorias =CategoriaSerializer(many = True)

    class Meta:
        model = EntidadeComunitaria
        fields = ('id', 'bairro', 'nome', 'endereco_oficial', 'endereco_usual', 'latitude', 'longitude', 'descricao', 'lista_de_categorias', 'imagem')
