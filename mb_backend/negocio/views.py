from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import EstabelecimentoFixoSerializer, EventoSerializer
from .models import EstabelecimentoFixo, Evento

# Create your views here.
class EstabelecimentoFixoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EstabelecimentoFixo.objects.all()
    serializer_class = EstabelecimentoFixoSerializer

class EstabelecimentoFixoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EstabelecimentoFixo.objects.all()
    serializer_class = EstabelecimentoFixoSerializer

class EstabelecimentoFixoInComunidade(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EstabelecimentoFixoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return EstabelecimentoFixo.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class EstabelecimentoFixoInTag(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EstabelecimentoFixoSerializer

    def get_queryset(self):
        tag = self.kwargs['pk']
        return EstabelecimentoFixo.objects.filter(listaTags__id=tag).order_by('id')


class EventoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EstabelecimentoFixo.objects.all()
    serializer_class = EventoSerializer

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EstabelecimentoFixo.objects.all()
    serializer_class = EventoSerializer

class EventoInComunidade(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EventoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Evento.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class EventoInTag(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EventoSerializer

    def get_queryset(self):
        tag = self.kwargs['pk']
        return Evento.objects.filter(listaTags__id=tag).order_by('id')
