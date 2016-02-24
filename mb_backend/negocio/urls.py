from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from negocio import views

urlpatterns = [
        url(r'^fixo/$',views.EstabelecimentoFixoList.as_view()),
        url(r'^fixo/(?P<pk>[0-9]+)/$',views.EstabelecimentoFixoDetail.as_view()),
        url(r'^fixo/comunidade/(?P<pk>[0-9]+)/$',views.EstabelecimentoFixoInComunidade.as_view()),
        url(r'^fixo/tag/(?P<pk>[0-9]+)/$',views.EstabelecimentoFixoInTag.as_view()),

        url(r'^evento/$',views.EventoList.as_view()),
        url(r'^evento/(?P<pk>[0-9]+)/$',views.EventoDetail.as_view()),
        url(r'^evento/comunidade/(?P<pk>[0-9]+)/$',views.EventoInComunidade.as_view()),
        url(r'^evento/tag/(?P<pk>[0-9]+)/$',views.EventoInTag.as_view()),

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
