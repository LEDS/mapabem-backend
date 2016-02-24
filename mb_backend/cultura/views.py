from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import PontoTuristicoSerializer, ObraSerializer, ArtistaSerializer
from .models import PontoTuristico, Obra, Artista

# Create your views here.
class PontoTuristicoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoInComunidade(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return PontoTuristico.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class PontoTuristicoInTag(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        tag = self.kwargs['pk']
        return PontoTuristico.objects.filter(listaTags__id=tag).order_by('id')

class ObraList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class ObraDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class ObraInComunidade(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ObraSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Obra.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class ObraInTag(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        tag = self.kwargs['pk']
        return Obra.objects.filter(listaTags__id=tag).order_by('id')

class ArtistaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class ArtistaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class ArtistaInComunidade(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Artista.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class ArtistaInTag(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        tag = self.kwargs['pk']
        return Artista.objects.filter(listaTags__id=tag).order_by('id')
