from django.contrib import admin
from .models import Comunidade
from .models import Categoria
from negocio.models import Comercio
from cultura.models import ObraExposta, Artista, PontoReferenciaCultural



# Register your models here.
admin.site.register(Comunidade)
admin.site.register(Categoria)
admin.site.register(Comercio)
admin.site.register(ObraExposta)
admin.site.register(Artista)
admin.site.register(PontoReferenciaCultural)
