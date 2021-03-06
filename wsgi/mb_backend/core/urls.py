from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
        url(r'^todos/$',views.TodasEntidades.as_view()),
        url(r'^todos/bairro/(?P<pk>[0-9]+)/$',views.TodasEntidadesEmBairro.as_view()),
        url(r'^todos/categoria/(?P<pk>[0-9]+)/$',views.TodasEntidadesEmCategoria.as_view()),
        url(r'^todos/bairro/(?P<bairro_pk>[0-9]+)/categoria/(?P<categoria_pk>[0-9]+)/$',views.TodasEntidadesEmBairroEmCategoria.as_view()),


        url(r'^elemento/(?P<pk>[0-9]+)/$',views.ElementoEspecifico.as_view()),
        #url(r'^elemento/(?P<nome>\w+)/$',views.BuscarPorNome.as_view()), em implementacao


        url(r'^bairros/$',views.BairroList.as_view()),
        url(r'^categorias/$',views.CategoriaList.as_view()),




        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
