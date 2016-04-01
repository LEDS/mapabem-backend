from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComunidadeSerializer, CategoriaSerializer
from .models import Comunidade, Categoria



# Create your views here.

class Permissao():
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ComunidadeList(generics.ListCreateAPIView, Permissao):
    queryset = Comunidade.get_all()
    serializer_class = ComunidadeSerializer


class CategoriaList(generics.ListCreateAPIView, Permissao):
    queryset = Categoria.get_all()
    serializer_class = CategoriaSerializer
