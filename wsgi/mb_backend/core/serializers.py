from rest_framework import serializers
from .models import Comunidade, Ponto, Categoria, PontoReferenciaComercial,PontoReferenciaCultural
from negocio.models import Comercio
from negocio.serializers import ComercioSerializer
from cultura.models import Artista, Obra
from cultura.serializers import ArtistaSerializer, ObraSerializer

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ('id','nome')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nome')


# class PontoModelSerializer(serializers.RelatedField):
#     def to_native(self, value):
#
#         if isinstance(value, PontoReferenciaComercial):
#             ponto_referencia_comercial_s = PontoReferenciaComercialSerializer(instance=value)
#             return ponto_referencia_comercial_s.data
#
#         if isinstance(value, Comercio):
#             comercio_s = ComercioSerializer(instance=value)
#             return comercio_s.data
#
#         raise NotImplementedError
#
# class PontoSerializer(serializers.ModelSerializer):
#     nomeDoProprietario = PontoModelSerializer(many=True, read_only=True)
#     class Meta:
#         model = Ponto
#         fields = ('id', 'comunidade', 'nome', 'nomeDoProprietario','enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')


class PontoSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Ponto
        fields = ('id', 'comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')
        #fields = '__all__'



class PontoReferenciaCulturalSerializer(serializers.ModelSerializer):
    comunidadePonto = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = PontoReferenciaCultural
        fields = ('id', 'comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias', 'imagem')

class PontoReferenciaComercialSerializer(serializers.ModelSerializer):
    comunidadePonto = ComunidadeSerializer()
    listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = PontoReferenciaComercial
        fields = ('nomeDoProprietario',)
