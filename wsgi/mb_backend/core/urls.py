from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
        url(r'^pontos/$',views.PontoList.as_view()),
        url(r'^ponto/(?P<pk>[0-9]+)/$',views.PontoDetail.as_view()),

        url(r'^ponto/comunidade/(?P<pk>[0-9]+)/$',views.PontoEmComunidade.as_view()),
        url(r'^ponto/categoria/(?P<pk>[0-9]+)/$',views.PontoEmCategoria.as_view()),
        url(r'^ponto/comunidade/(?P<comunidade_pk>[0-9]+)/categoria/(?P<categoria_pk>[0-9]+)/$',views.PontoEmComunidadeEmCategoria.as_view()),

        url(r'^comunidades/$',views.ComunidadeList.as_view()),
        url(r'^categorias/$',views.CategoriaList.as_view()),


        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
