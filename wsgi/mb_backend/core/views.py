from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComunidadeSerializer, PontoSerializer, CategoriaSerializer
from .models import Comunidade, Ponto, Categoria


# Create your views here.

class Permissao():
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ComunidadeList(generics.ListCreateAPIView, Permissao):
    queryset = Comunidade.get_all()
    serializer_class = ComunidadeSerializer

class PontoEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = PontoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']

        return Ponto.get_ponto_em_comunidade(comunidade)

class CategoriaList(generics.ListCreateAPIView, Permissao):
    queryset = Categoria.get_all()
    serializer_class = CategoriaSerializer

class PontoEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = PontoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Ponto.get_ponto_em_categoria(categoria)


class PontoList(generics.ListCreateAPIView, Permissao):
    queryset = Ponto.get_all()
    serializer_class = PontoSerializer

class PontoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Ponto.get_all()
    serializer_class = PontoSerializer



class PontoEmComunidadeEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = PontoSerializer

    def get_queryset(self):
        categoria = self.kwargs['categoria_pk']
        comunidade= self.kwargs['comunidade_pk']
        return Ponto.get_ponto_em_comunidade_em_categoria(comunidade, categoria)
