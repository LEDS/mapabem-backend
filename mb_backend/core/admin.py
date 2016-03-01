from django.contrib import admin
from .models import Comunidade
from .models import Categoria
from negocio.models import EstabelecimentoFixo
from negocio.models import Datas
from negocio.models import Evento
from cultura.models import Artista
from cultura.models import Obra
from cultura.models import PontoTuristico


# Register your models here.
admin.site.register(Comunidade)
admin.site.register(Categoria)
admin.site.register(PontoTuristico)
admin.site.register(EstabelecimentoFixo)
admin.site.register(Datas)
admin.site.register(Artista)
admin.site.register(Obra)
