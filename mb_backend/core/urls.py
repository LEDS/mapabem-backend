from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
        url(r'^$', views.elemento_list),
        url(r'^elemento/$',views.ElementoList.as_view()),
        url(r'^elemento/(?P<pk>[0-9]+)/$',views.ElementoDetail.as_view()),

        url(r'^elemento/comunidade/(?P<pk>[0-9]+)/$',views.ElementoInComunidade.as_view()),
        url(r'^elemento/tag/(?P<pk>[0-9]+)/$',views.ElementoInTag.as_view()),

        url(r'^comunidade/$',views.ComunidadeList.as_view()),
        url(r'^tag/$',views.TagList.as_view()),


        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)