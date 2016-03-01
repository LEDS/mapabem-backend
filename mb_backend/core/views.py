from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComunidadeSerializer, ElementoSerializer, CategoriaSerializer
from .models import Comunidade, Elemento, Categoria



# Create your views here.
def elemento_list(request):
    elementos = Elemento.objects.all()
    return render(request, 'core/index.html', {'elementos' : elementos})



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

class CategoriaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ElementoInCategoria(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ElementoSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Elemento.objects.filter(listaCategorias__id=categoria).order_by('id')


class ElementoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer

class ElementoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
