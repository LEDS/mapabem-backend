from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComunidadeSerializer, ElementoSerializer, TagSerializer
from .models import Comunidade, Elemento, Tag


# Create your views here.
class ComunidadeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer

class ElementoInComunidade(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ElementoSerializer

    def get_queryset(self):
        comunidade = self.kwargs['pk']
        return Elemento.objects.filter(comunidadeElemento_id=comunidade).order_by('id')

class TagList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ElementoInTag(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ElementoSerializer

    def get_queryset(self):
        tag = self.kwargs['pk']
        return Elemento.objects.filter(listaTags__id=tag).order_by('id')


class ElementoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer

class ElementoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
