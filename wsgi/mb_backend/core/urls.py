from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
        url(r'^comunidades/$',views.ComunidadeList.as_view()),
        url(r'^categorias/$',views.CategoriaList.as_view()),


        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
