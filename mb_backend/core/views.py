from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from .serializers import ComunidadeSerializer, ElementoSerializer, CategoriaSerializer
from .models import Comunidade, Elemento, Categoria

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




# Create your views here.

class ComunidadeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #queryset = Comunidade.getAll() problema, no models -> self is not defined -> com o self da erro informando que falando que o objeto nao existe
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
    #queryset = Categoria.getAll() problema, no models -> self is not defined -> com o self da erro informando que falando que o objeto nao existe
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
    #queryset = Elemento.getAll(elemento)
    queryset = Elemento.objects.all()

    serializer_class = ElementoSerializer

class ElementoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #queryset = Elemento.getAll(elemento) problema, no models -> self is not defined -> com o self da erro informando que falando que o objeto nao existe
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



@csrf_exempt
def elemento_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        #elemento = Elemento.getAll(elemento) problema, no models -> self is not defined -> com o self da erro informando que falando que o objeto nao existe
        elemento = Elemento.objects.all()
        serializer = ElementoSerializer(elemento, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def elemento_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        elemento = Elemento.objects.get(pk=pk)
    except Elemento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ElementoSerializer(elemento)
        return JSONResponse(serializer.data)
