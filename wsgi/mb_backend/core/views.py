from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from drf_multiple_model.views import MultipleModelAPIView

from .serializers import BairroSerializer, CategoriaSerializer
from negocio.serializers import ComercioSerializer, ComercioSerializerBasic
from cultura.serializers import ObraExpostaSerializer, ArtistaSerializer, PontoReferenciaCulturalSerializer, ObraExpostaSerializerBasic, ArtistaSerializerBasic, PontoReferenciaCulturalSerializerBasic

from .models import Bairro, Categoria
from cultura.models import ObraExposta, Artista, PontoReferenciaCultural
from negocio.models import Comercio



# Create your views here.

class Permissao():
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BairroList(generics.ListCreateAPIView, Permissao):
    queryset = Bairro.get_all()
    serializer_class = BairroSerializer


class CategoriaList(generics.ListCreateAPIView, Permissao):
    queryset = Categoria.get_all()
    serializer_class = CategoriaSerializer

class TodasEntidadesEmBairro(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    # normalmente e utilizado o metodo query_set porem para que fossem feitas buscas em varios objetos e como resultado fosse gerada
    # apenas uma lista foi utilizada o APP externo "drf_multiple_model"
    def get_queryList(self):
        bairro = self.kwargs['pk']
        queryList = [
            (Comercio.get_comercio_em_bairro(bairro),ComercioSerializerBasic),
            (ObraExposta.get_obra_exposta_em_bairro(bairro), ObraExpostaSerializerBasic),
            (Artista.get_artista_em_bairro(bairro), ArtistaSerializerBasic),
            (PontoReferenciaCultural.get_ponto_referencia_cultural_em_bairro(bairro), PontoReferenciaCulturalSerializerBasic)
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

class TodasEntidadesEmBairroEmCategoria(MultipleModelAPIView, Permissao):
    flat = True
    add_model_type = False
    def get_queryList(self):
        bairro = self.kwargs['bairro_pk']
        categoria = self.kwargs['categoria_pk']
        queryList = [
            (Comercio.get_comercio_em_bairro_em_categoria(bairro, categoria),ComercioSerializerBasic),
            (ObraExposta.get_obra_exposta_em_bairro_em_categoria(bairro, categoria), ObraExpostaSerializerBasic),
            (Artista.get_artista_em_bairro_em_categoria(bairro, categoria), ArtistaSerializerBasic),
            (PontoReferenciaCultural.get_ponto_referencia_cultural_em_bairro_em_categoria(bairro, categoria), PontoReferenciaCulturalSerializerBasic)
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

# em implementacao
# class BuscarPorNome(MultipleModelAPIView, Permissao):
#     flat = True
#     add_model_type = False
#     def get_queryList(self):
#         nome = self.kwargs['nome']
#         queryList = [
#             (Comercio.get_por_nome(nome),ComercioSerializerBasic),
#             (ObraExposta.get_por_nome(nome), ObraExpostaSerializerBasic),
#             (Artista.get_por_nome(nome), ArtistaSerializerBasic),
#             (PontoReferenciaCultural.get_por_nome(nome), PontoReferenciaCulturalSerializerBasic)
#         ]
#         return queryList
