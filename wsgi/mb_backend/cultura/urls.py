from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from cultura import views

urlpatterns = [
        url(r'^pontoturistico/$',views.PontoTuristicoList.as_view()),
        url(r'^pontoturistico/(?P<pk>[0-9]+)/$',views.PontoTuristicoDetail.as_view()),
        url(r'^pontoturistico/comunidade/(?P<pk>[0-9]+)/$',views.PontoTuristicoEmComunidade.as_view()),
        url(r'^pontoturistico/categoria/(?P<pk>[0-9]+)/$',views.PontoTuristicoEmCategoria.as_view()),

        url(r'^artista/$',views.ArtistaList.as_view()),
        url(r'^artista/(?P<pk>[0-9]+)/$',views.ArtistaDetail.as_view()),
        url(r'^artista/comunidade/(?P<pk>[0-9]+)/$',views.ArtistaEmComunidade.as_view()),
        url(r'^artista/categoria/(?P<pk>[0-9]+)/$',views.ArtistaEmCategoria.as_view()),

        url(r'^obra/$',views.ObraList.as_view()),
        url(r'^obra/(?P<pk>[0-9]+)/$',views.ObraDetail.as_view()),
        url(r'^obra/comunidade/(?P<pk>[0-9]+)/$',views.ObraEmComunidade.as_view()),
        url(r'^obra/categoria/(?P<pk>[0-9]+)/$',views.ObraEmCategoria.as_view()),



        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
