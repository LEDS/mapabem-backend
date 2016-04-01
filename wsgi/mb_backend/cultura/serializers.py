from rest_framework import serializers
from .models import ObraExposta, Artista, PontoReferenciaCultural
from core.serializers import ComunidadeSerializer, CategoriaSerializer

class ObraExpostaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)
    class Meta:
        model = ObraExposta
        fields = ('id', 'comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')

class ObraExpostaSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = ObraExposta
        fields = ('id', 'nome', 'descricao', 'imagem')

class ArtistaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)
    listaObras = ObraExpostaSerializer(many = True)
    class Meta:
        model = Artista
        fields = ('id','comunidade', 'nome','telefone', 'descricao', 'listaObras', 'listaCategorias', 'imagem')


class ArtistaSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = ObraExposta
        fields = ('id', 'nome', 'descricao', 'imagem')


class PontoReferenciaCulturalSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)
    class Meta:
        model = PontoReferenciaCultural
        fields = ('id','comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias')


class PontoReferenciaCulturalSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = ObraExposta
        fields = ('id', 'nome', 'descricao', 'imagem')
