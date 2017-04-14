from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from cultura import views

urlpatterns = [

        # url(r'^artistas/$',views.ArtistaList.as_view()),
        # url(r'^artista/(?P<pk>[0-9]+)/$',views.ArtistaDetail.as_view()),
        # url(r'^artista/bairro/(?P<pk>[0-9]+)/$',views.ArtistaEmBairro.as_view()),
        # url(r'^artista/categoria/(?P<pk>[0-9]+)/$',views.ArtistaEmCategoria.as_view()),
        # url(r'^artista/bairro/(?P<bairro_pk>[0-9]+)/categoria/(?P<categoria_pk>[0-9]+)/$',views.ArtistaEmCategoriaEmBairro.as_view()),
        #
        # url(r'^obras/$',views.ObraExpostaList.as_view()),
        # url(r'^obra/(?P<pk>[0-9]+)/$',views.ObraExpostaDetail.as_view()),
        # url(r'^obra/bairro/(?P<pk>[0-9]+)/$',views.ObraExpostaEmBairro.as_view()),
        # url(r'^obra/categoria/(?P<pk>[0-9]+)/$',views.ObraExpostaEmCategoria.as_view()),
        # url(r'^obra/bairro/(?P<bairro_pk>[0-9]+)/categoria/(?P<categoria_pk>[0-9]+)/$',views.ObraExpostaEmCategoriaEmBairro.as_view()),
        #
        # url(r'^pontosculturais/$',views.PontoReferenciaCulturalList.as_view()),
        # url(r'^pontocultural/(?P<pk>[0-9]+)/$',views.ObraExpostaDetail.as_view()),
        # url(r'^pontocultural/bairro/(?P<pk>[0-9]+)/$',views.ObraExpostaEmBairro.as_view()),
        # url(r'^pontocultural/categoria/(?P<pk>[0-9]+)/$',views.ObraExpostaEmCategoria.as_view()),
        # url(r'^pontocultural/bairro/(?P<bairro_pk>[0-9]+)/categoria/(?P<categoria_pk>[0-9]+)/$',views.ObraExpostaEmCategoriaEmBairro.as_view()),
        #

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
