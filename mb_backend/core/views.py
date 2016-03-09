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
    queryset = Comunidade.getAll()
    serializer_class = ComunidadeSerializer

class ElementoInComunidade(generics.ListAPIView, Permissao):
    serializer_class = ElementoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']

        return Elemento.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class CategoriaList(generics.ListCreateAPIView, Permissao):
    queryset = Categoria.getAll()
    serializer_class = CategoriaSerializer

class ElementoInCategoria(generics.ListAPIView, Permissao):
    serializer_class = ElementoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Elemento.objects.filter(listaCategorias__id=categoria).order_by('id')


class ElementoList(generics.ListCreateAPIView, Permissao):
    queryset = Elemento.getAll()
    serializer_class = ElementoSerializer

class ElementoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Elemento.getAll()
    serializer_class = ElementoSerializer
