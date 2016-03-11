from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import EstabelecimentoFixoSerializer, EventoSerializer
from .models import EstabelecimentoFixo, Evento
from core.views import Permissao

# Create your views here.

class EstabelecimentoFixoList(generics.ListCreateAPIView, Permissao):
    queryset = EstabelecimentoFixo.getAll()
    serializer_class = EstabelecimentoFixoSerializer

class EstabelecimentoFixoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = EstabelecimentoFixo.getAll()
    serializer_class = EstabelecimentoFixoSerializer

class EstabelecimentoFixoInComunidade(generics.ListAPIView, Permissao):
    serializer_class = EstabelecimentoFixoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return EstabelecimentoFixo.getEstabelecimentoFixoInComunidade(comunidade)

class EstabelecimentoFixoInTag(generics.ListAPIView, Permissao):
    serializer_class = EstabelecimentoFixoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return EstabelecimentoFixo.getEstabelecimentoFixoInCategoria(categoria)


class EventoList(generics.ListCreateAPIView, Permissao):
    queryset = Evento.getAll()
    serializer_class = EventoSerializer

class EventoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Evento.getAll()
    serializer_class = EventoSerializer

class EventoInComunidade(generics.ListAPIView, Permissao):
    serializer_class = EventoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Evento.getEventoInComunidade(comunidade)

class EventoInTag(generics.ListAPIView, Permissao):
    serializer_class = EventoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Evento.getPEventoInCategoria(categoria)
