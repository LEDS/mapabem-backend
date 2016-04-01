from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComercioSerializer
from .models import Comercio
from core.views import Permissao


# Create your views here.

class ComercioList(generics.ListCreateAPIView, Permissao):
    queryset = Comercio.get_all()
    serializer_class = ComercioSerializer

class ComercioDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Comercio.get_all()
    serializer_class = ComercioSerializer

class ComercioEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ComercioSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Comercio.get_comercio_em_comunidade(comunidade)

class ComercioEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ComercioSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Comercio.get_comercio_em_categoria(categoria)

class ComercioEmComunidadeEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ComercioSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        categoria = self.kwargs['pk']
        return Comercio.get_comercio_em_comunidade_em_categoria(comunidade, categoria)
