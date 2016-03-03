from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
        #url(r'^elemento/$',views.ElementoList.as_view()),
        #url(r'^elemento/id/(?P<pk>[0-9]+)/$',views.ElementoDetail.as_view()),
        #url(r'^elemento/uuid/(?P<elementouuid>[\w.@+-]+)/$', views.ElementoDetailUUID.as_view()),
        url(r'^elemento/$',views.elemento_list),
        url(r'^elemento/id/(?P<pk>[0-9]+)/$',views.elemento_detail),

        url(r'^elemento/comunidade/(?P<pk>[0-9]+)/$',views.ElementoInComunidade.as_view()),
        url(r'^elemento/categoria/(?P<pk>[0-9]+)/$',views.ElementoInCategoria.as_view()),

        url(r'^comunidade/$',views.ComunidadeList.as_view()),
        url(r'^categoria/$',views.CategoriaList.as_view()),


        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
