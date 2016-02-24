from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from cultura import views

urlpatterns = [
        url(r'^pontoturistico/$',views.PontoTuristicoList.as_view()),
        url(r'^pontoturistico/(?P<pk>[0-9]+)/$',views.PontoTuristicoDetail.as_view()),
        url(r'^pontoturistico/comunidade/(?P<pk>[0-9]+)/$',views.PontoTuristicoInComunidade.as_view()),
        url(r'^pontoturistico/tag/(?P<pk>[0-9]+)/$',views.PontoTuristicoInTag.as_view()),

        url(r'^artista/$',views.ArtistaList.as_view()),
        url(r'^artista/(?P<pk>[0-9]+)/$',views.ArtistaDetail.as_view()),
        url(r'^artista/comunidade/(?P<pk>[0-9]+)/$',views.ArtistaInComunidade.as_view()),
        url(r'^artista/tag/(?P<pk>[0-9]+)/$',views.ArtistaInTag.as_view()),

        url(r'^obra/$',views.ObraList.as_view()),
        url(r'^obra/(?P<pk>[0-9]+)/$',views.ObraDetail.as_view()),
        url(r'^obra/comunidade/(?P<pk>[0-9]+)/$',views.ObraInComunidade.as_view()),
        url(r'^obra/tag/(?P<pk>[0-9]+)/$',views.ObraInTag.as_view()),



        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
