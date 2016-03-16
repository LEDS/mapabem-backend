from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComunidadeSerializer, ElementoSerializer, CategoriaSerializer
from .models import Comunidade, Elemento, Categoria


# Create your views here.

class Permissao():
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ComunidadeList(generics.ListCreateAPIView, Permissao):
    queryset = Comunidade.get_all()
    serializer_class = ComunidadeSerializer

class ElementoEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ElementoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']

        return Elemento.get_elemento_em_comunidade(comunidade)

class CategoriaList(generics.ListCreateAPIView, Permissao):
    queryset = Categoria.get_all()
    serializer_class = CategoriaSerializer

class ElementoEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ElementoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Elemento.get_elemento_em_categoria(categoria)


class ElementoList(generics.ListCreateAPIView, Permissao):
    queryset = Elemento.get_all()
    serializer_class = ElementoSerializer

class ElementoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Elemento.get_all()
    serializer_class = ElementoSerializer



class ElementoEmComunidadeEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ElementoSerializer

    def get_queryset(self):
        categoria = self.kwargs['categoria_pk']
        comunidade= self.kwargs['comunidade_pk']
        return Elemento.get_elemento_em_comunidade_em_categoria(comunidade, categoria)
