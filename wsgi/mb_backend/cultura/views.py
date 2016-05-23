from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ObraExpostaSerializer, ArtistaSerializer, PontoReferenciaCulturalSerializer, ObraExpostaSerializerBasic, ArtistaSerializerBasic, PontoReferenciaCulturalSerializerBasic
from .models import ObraExposta, Artista, PontoReferenciaCultural
from core.views import Permissao


# Create your views here.
#
# class ObraExpostaList(generics.ListCreateAPIView, Permissao):
#     queryset = ObraExposta.get_all()
#     serializer_class = ObraExpostaSerializerBasic
#
# class ObraExpostaDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
#     queryset = ObraExposta.get_all()
#     serializer_class = ObraExpostaSerializer
#
# class ObraExpostaEmBairro(generics.ListAPIView, Permissao):
#     serializer_class = ObraExpostaSerializerBasic
#
#     def get_queryset(self):
#         bairro = self.kwargs['pk']
#         return ObraExposta.get_obra_exposta_em_bairro(bairro)
#
# class ObraExpostaEmCategoria(generics.ListAPIView, Permissao):
#     serializer_class = ObraExpostaSerializerBasic
#     def get_queryset(self):
#         categoria = self.kwargs['pk']
#         return Obra.get_obra_exposta_em_categoria(categoria)
#
# class ObraExpostaEmCategoriaEmBairro(generics.ListAPIView, Permissao):
#     serializer_class = ObraExpostaSerializerBasic
#     def get_queryset(self):
#         bairro = self.kwargs['pk']
#         categoria = self.kwargs['pk']
#         return Obra.get_obra_exposta_em_bairro_em_categoria(bairro, categoria)
#
# ######################################################################
#
# class ArtistaList(generics.ListCreateAPIView, Permissao):
#     queryset = Artista.get_all()
#     serializer_class = ArtistaSerializerBasic
#
# class ArtistaDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
#     queryset = Artista.get_all()
#     serializer_class = ArtistaSerializer
#
# class ArtistaEmBairro(generics.ListAPIView, Permissao):
#     serializer_class = ArtistaSerializerBasic
#
#     def get_queryset(self):
#         bairro = self.kwargs['pk']
#         return Artista.get_artista_em_bairro(bairro)
#
# class ArtistaEmCategoria(generics.ListAPIView, Permissao):
#     serializer_class = ArtistaSerializerBasic
#
#     def get_queryset(self):
#         categoria = self.kwargs['pk']
#         return Artista.get_artista_em_categoria(categoria)
#
# class ArtistaEmCategoriaEmBairro(generics.ListAPIView, Permissao):
#     serializer_class = ArtistaSerializerBasic
#     def get_queryset(self):
#         bairro = self.kwargs['pk']
#         categoria = self.kwargs['pk']
#         return Artista.get_artista_em_bairro_em_categoria(bairro, categoria)
#
# #########################################################################
#
# class PontoReferenciaCulturalList(generics.ListCreateAPIView, Permissao):
#     queryset = PontoReferenciaCultural.get_all()
#     serializer_class = PontoReferenciaCulturalSerializerBasic
#
# class PontoReferenciaCulturalDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
#     queryset = PontoReferenciaCultural.get_all()
#     serializer_class = PontoReferenciaCulturalSerializer
#
# class PontoReferenciaCulturalEmBairro(generics.ListAPIView, Permissao):
#     serializer_class = PontoReferenciaCulturalSerializerBasic
#
#     def get_queryset(self):
#         bairro = self.kwargs['pk']
#         return PontoReferenciaCultural.get_ponto_referencia_cultural_em_bairro(bairro)
#
# class PontoReferenciaCulturalEmCategoria(generics.ListAPIView, Permissao):
#     serializer_class = PontoReferenciaCulturalSerializerBasic
#
#     def get_queryset(self):
#         categoria = self.kwargs['pk']
#         return PontoReferenciaCultural.get_ponto_referencia_cultural_em_categoria(categoria)
#
# class PontoReferenciaCulturalEmCategoriaEmBairro(generics.ListAPIView, Permissao):
#     serializer_class = PontoReferenciaCulturalSerializerBasic
#     def get_queryset(self):
#         bairro = self.kwargs['pk']
#         categoria = self.kwargs['pk']
#         return PontoReferenciaCultural.get_ponto_referencia_cultural_em_bairro_em_categoria(bairro, categoria)
