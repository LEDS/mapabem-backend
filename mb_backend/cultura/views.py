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
    queryset = PontoTuristico.getAll()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = PontoTuristico.getAll()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoInComunidade(generics.ListAPIView, Permissao):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return PontoTuristico.getPontoTuristicoInComunidade(comunidade)

class PontoTuristicoInTag(generics.ListAPIView, Permissao):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return PontoTuristico.getPontoTuristicoInCategoria(categoria)

class ObraList(generics.ListCreateAPIView, Permissao):
    queryset = Obra.getAll()
    serializer_class = ObraSerializer

class ObraDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Obra.getAll()
    serializer_class = ObraSerializer

class ObraInComunidade(generics.ListAPIView, Permissao):
    serializer_class = ObraSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Obra.getObraInComunidade(comunidade)

class ObraInTag(generics.ListAPIView, Permissao):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Obra.getObraInCategoria(categoria)

class ArtistaList(generics.ListCreateAPIView, Permissao):
    queryset = Artista.getAll()
    serializer_class = ArtistaSerializer

class ArtistaDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Artista.getAll()
    serializer_class = ArtistaSerializer

class ArtistaInComunidade(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Artista.getArtistaInComunidade(comunidade)

class ArtistaInTag(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Artista.getArtistaInCategoria(categoria)
