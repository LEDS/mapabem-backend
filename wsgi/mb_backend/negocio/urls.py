from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from negocio import views

urlpatterns = [
        url(r'^comercio/$',views.ComercioList.as_view()),
        url(r'^comercio/(?P<pk>[0-9]+)/$',views.ComercioDetail.as_view()),
        url(r'^comercio/comunidade/(?P<pk>[0-9]+)/$',views.ComercioEmComunidade.as_view()),
        url(r'^comercio/categoria/(?P<pk>[0-9]+)/$',views.ComercioEmCategoria.as_view()),
        url(r'^comercio/comunidade/(?P<comunidade_pk>[0-9]+)/categoria/(?P<categoria_pk>[0-9]+)/$',views.ComercioEmComunidadeEmCategoria.as_view()),

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
