from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import PontoTuristicoSerializer, ObraSerializer, ArtistaSerializer
from .models import PontoTuristico, Obra, Artista
from core.views import Permissao


# Create your views here.
class PontoTuristicoList(generics.ListCreateAPIView, Permissao):
    queryset = PontoTuristico.get_all()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = PontoTuristico.get_all()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoEmComunidade(generics.ListAPIView, Permissao):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return PontoTuristico.get_pontoturistico_em_comunidade(comunidade)

class PontoTuristicoEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return PontoTuristico.get_pontoturistico_em_categoria(categoria)

class ObraList(generics.ListCreateAPIView, Permissao):
    queryset = Obra.get_all()
    serializer_class = ObraSerializer

class ObraDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Obra.get_all()
    serializer_class = ObraSerializer

class ObraEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ObraSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Obra.get_obra_em_comunidade(comunidade)

class ObraEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Obra.get_obra_em_categoria(categoria)

class ArtistaList(generics.ListCreateAPIView, Permissao):
    queryset = Artista.get_all()
    serializer_class = ArtistaSerializer

class ArtistaDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Artista.get_all()
    serializer_class = ArtistaSerializer

class ArtistaEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Artista.get_artista_em_comunidade(comunidade)

class ArtistaEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Artista.get_artista_em_categoria(categoria)