from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
        url(r'^elementos/$',views.ElementoList.as_view()),
        url(r'^elemento/(?P<pk>[0-9]+)/$',views.ElementoDetail.as_view()),

        url(r'^elemento/comunidade/(?P<pk>[0-9]+)/$',views.ElementoInComunidade.as_view()),
        url(r'^elemento/categoria/(?P<pk>[0-9]+)/$',views.ElementoInCategoria.as_view()),

        url(r'^comunidades/$',views.ComunidadeList.as_view()),
        url(r'^categorias/$',views.CategoriaList.as_view()),


        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
