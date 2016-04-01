from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ObraExpostaSerializer, ArtistaSerializer, PontoReferenciaCulturalSerializer
from .models import ObraExposta, Artista, PontoReferenciaCultural
from core.views import Permissao


# Create your views here.

class ObraExpostaList(generics.ListCreateAPIView, Permissao):
    queryset = ObraExposta.get_all()
    serializer_class = ObraExpostaSerializer

class ObraExpostaDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = ObraExposta.get_all()
    serializer_class = ObraExpostaSerializer

class ObraExpostaEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ObraExpostaSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return ObraExposta.get_obra_exposta_em_comunidade(comunidade)

class ObraExpostaEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ObraExpostaSerializer
    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Obra.get_obra_exposta_em_categoria(categoria)

class ObraExpostaEmCategoriaEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ObraExpostaSerializer
    def get_queryset(self):
        comunidade = self.kwargs['pk']
        categoria = self.kwargs['pk']
        return Obra.get_obra_exposta_em_comunidade_em_categoria(comunidade, categoria)

######################################################################

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

class ArtistaEmCategoriaEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer
    def get_queryset(self):
        comunidade = self.kwargs['pk']
        categoria = self.kwargs['pk']
        return Artista.get_artista_em_comunidade_em_categoria(comunidade, categoria)

#########################################################################

class PontoReferenciaCulturalList(generics.ListCreateAPIView, Permissao):
    queryset = PontoReferenciaCultural.get_all()
    serializer_class = PontoReferenciaCulturalSerializer

class PontoReferenciaCulturalDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = PontoReferenciaCultural.get_all()
    serializer_class = PontoReferenciaCulturalSerializer

class PontoReferenciaCulturalEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = PontoReferenciaCulturalSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return PontoReferenciaCultural.get_ponto_referencia_cultural_em_comunidade(comunidade)

class PontoReferenciaCulturalEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return PontoReferenciaCultural.get_ponto_referencia_cultural_em_categoria(categoria)

class PontoReferenciaCulturalEmCategoriaEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = ArtistaSerializer
    def get_queryset(self):
        comunidade = self.kwargs['pk']
        categoria = self.kwargs['pk']
        return PontoReferenciaCultural.get_ponto_referencia_cultural_em_comunidade_em_categoria(comunidade, categoria)
