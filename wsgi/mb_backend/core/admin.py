from django.contrib import admin
from .models import Comunidade
from .models import Categoria
from .models import PontoReferenciaComercial
from .models import PontoReferenciaCultural
from negocio.models import Comercio
from cultura.models import Artista
from cultura.models import Obra


# Register your models here.
admin.site.register(Comunidade)
admin.site.register(Categoria)
admin.site.register(Comercio)
admin.site.register(Artista)
admin.site.register(Obra)
admin.site.register(PontoReferenciaComercial)
admin.site.register(PontoReferenciaCultural)
