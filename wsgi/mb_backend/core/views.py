from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from drf_multiple_model.views import MultipleModelAPIView

from .serializers import ComunidadeSerializer, CategoriaSerializer
from negocio.serializers import ComercioSerializer, ComercioSerializerBasic
from cultura.serializers import ObraExpostaSerializer, ArtistaSerializer, PontoReferenciaCulturalSerializer, ObraExpostaSerializerBasic, ArtistaSerializerBasic, PontoReferenciaCulturalSerializerBasic

from .models import Comunidade, Categoria
from cultura.models import ObraExposta, Artista, PontoReferenciaCultural
from negocio.models import Comercio



# Create your views here.

class Permissao():
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ComunidadeList(generics.ListCreateAPIView, Permissao):
    queryset = Comunidade.get_all()
    serializer_class = ComunidadeSerializer


class CategoriaList(generics.ListCreateAPIView, Permissao):
    queryset = Categoria.get_all()
    serializer_class = CategoriaSerializer

class TodasEntidadesEmComunidade(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        comunidade = self.kwargs['pk']
        queryList = [
            (Comercio.get_comercio_em_comunidade(comunidade),ComercioSerializerBasic),
            (ObraExposta.get_obra_exposta_em_comunidade(comunidade), ObraExpostaSerializerBasic),
            (Artista.get_artista_em_comunidade(comunidade), ArtistaSerializerBasic),
            (PontoReferenciaCultural.get_ponto_referencia_cultural_em_comunidade(comunidade), PontoReferenciaCulturalSerializerBasic)
        ]
        return queryList


class TodasEntidadesEmCategoria(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        categoria = self.kwargs['pk']
        queryList = [
            (Comercio.get_comercio_em_categoria(categoria),ComercioSerializerBasic),
            (ObraExposta.get_obra_exposta_em_categoria(categoria), ObraExpostaSerializerBasic),
            (Artista.get_artista_em_categoria(categoria), ArtistaSerializerBasic),
            (PontoReferenciaCultural.get_ponto_referencia_cultural_em_categoria(categoria), PontoReferenciaCulturalSerializerBasic)
        ]
        return queryList

class TodasEntidadesEmComunidadeEmCategoria(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        comunidade = self.kwargs['comunidade_pk']
        categoria = self.kwargs['categoria_pk']
        queryList = [
            (Comercio.get_comercio_em_comunidade_em_categoria(comunidade, categoria),ComercioSerializerBasic),
            (ObraExposta.get_obra_exposta_em_comunidade_em_categoria(comunidade, categoria), ObraExpostaSerializerBasic),
            (Artista.get_artista_em_comunidade_em_categoria(comunidade, categoria), ArtistaSerializerBasic),
            (PontoReferenciaCultural.get_ponto_referencia_cultural_em_comunidade_em_categoria(comunidade, categoria), PontoReferenciaCulturalSerializerBasic)
        ]
        return queryList


class ElementoEspecifico(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        identificador = self.kwargs['pk']
        queryList = [
            (Comercio.get_por_id(identificador),ComercioSerializer),
            (ObraExposta.get_por_id(identificador), ObraExpostaSerializer),
            (Artista.get_por_id(identificador), ArtistaSerializer),
            (PontoReferenciaCultural.get_por_id(identificador), PontoReferenciaCulturalSerializer)
        ]
        return queryList


class TodasEntidades(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        queryList = [
            (Comercio.get_all(),ComercioSerializer),
            (ObraExposta.get_all(), ObraExpostaSerializer),
            (Artista.get_all(), ArtistaSerializer),
            (PontoReferenciaCultural.get_all(), PontoReferenciaCulturalSerializer)
        ]
        return queryList


class BuscarPorNome(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        nome = self.kwargs['nome']
        queryList = [
            (Comercio.get_por_nome(nome),ComercioSerializerBasic),
            (ObraExposta.get_por_nome(nome), ObraExpostaSerializerBasic),
            (Artista.get_por_nome(nome), ArtistaSerializerBasic),
            (PontoReferenciaCultural.get_por_nome(nome), PontoReferenciaCulturalSerializerBasic)
        ]
        return queryList
