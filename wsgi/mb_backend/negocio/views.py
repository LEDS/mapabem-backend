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
    queryset = EstabelecimentoFixo.get_all()
    serializer_class = EstabelecimentoFixoSerializer

class EstabelecimentoFixoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = EstabelecimentoFixo.get_all()
    serializer_class = EstabelecimentoFixoSerializer

class EstabelecimentoFixoEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = EstabelecimentoFixoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return EstabelecimentoFixo.get_estabelecimentofixo_em_comunidade(comunidade)

class EstabelecimentoFixoEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = EstabelecimentoFixoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return EstabelecimentoFixo.get_estabelecimentofixo_em_categoria(categoria)


class EventoList(generics.ListCreateAPIView, Permissao):
    queryset = Evento.get_all()
    serializer_class = EventoSerializer

class EventoDetail(generics.RetrieveUpdateDestroyAPIView, Permissao):
    queryset = Evento.get_all()
    serializer_class = EventoSerializer

class EventoEmComunidade(generics.ListAPIView, Permissao):
    serializer_class = EventoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Evento.get_evento_em_comunidade(comunidade)

class EventoEmCategoria(generics.ListAPIView, Permissao):
    serializer_class = EventoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Evento.get_evento_em_categoria(categoria)
