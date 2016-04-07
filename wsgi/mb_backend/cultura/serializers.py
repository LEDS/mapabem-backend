from rest_framework import serializers
from .models import ObraExposta, Artista, PontoReferenciaCultural
from core.serializers import ComunidadeSerializer, CategoriaSerializer

class ObraExpostaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    lista_de_categorias =CategoriaSerializer(many = True)
    class Meta:
        model = ObraExposta
        fields = ('id', 'comunidade', 'nome', 'endereco_oficial', 'endereco_usual', 'latitude', 'longitude', 'descricao', 'lista_de_categorias', 'imagem')

class ObraExpostaSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = ObraExposta
        fields = ('id', 'nome', 'descricao', 'imagem')

class ArtistaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    lista_de_categorias =CategoriaSerializer(many = True)
    lista_de_obras = ObraExpostaSerializer(many = True)
    class Meta:
        model = Artista
        fields = ('id','comunidade', 'nome','telefone', 'descricao', 'lista_de_obras', 'lista_de_categorias', 'imagem')


class ArtistaSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = ObraExposta
        fields = ('id', 'nome', 'descricao', 'imagem')


class PontoReferenciaCulturalSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    lista_de_categorias =CategoriaSerializer(many = True)
    class Meta:
        model = PontoReferenciaCultural
        fields = ('id','comunidade', 'nome', 'endereco_oficial', 'endereco_usual', 'latitude', 'longitude', 'descricao', 'lista_de_categorias')


class PontoReferenciaCulturalSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = ObraExposta
        fields = ('id', 'nome', 'descricao', 'imagem')
