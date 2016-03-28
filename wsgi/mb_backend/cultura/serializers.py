from rest_framework import serializers
from .models import Obra, Artista
#from core.serializers import ComunidadeSerializer, CategoriaSerializer

class ObraSerializer(serializers.ModelSerializer):
    # comunidade = ComunidadeSerializer()
    # listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Obra
        fields = ('id', 'comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaCategorias')

class ArtistaSerializer(serializers.ModelSerializer):
    # comunidade = ComunidadeSerializer()
    # listaCategorias =CategoriaSerializer(many = True)
    listaObras = ObraSerializer(many = True)

    class Meta:
        model = Artista
        fields = ('id','comunidade', 'nome', 'enderecoOficial', 'enderecoUsual', 'latitude', 'longitude', 'descricao', 'listaObras', 'listaCategorias')
