from django.contrib import admin
from .models import Comunidade
from .models import Tag
from .models import Localizacao
from .models import PontoTuristico
from .models import EstabelecimentoFixo
from .models import Datas


# Register your models here.
admin.site.register(Comunidade)
admin.site.register(Tag)
admin.site.register(Localizacao)
admin.site.register(PontoTuristico)
admin.site.register(EstabelecimentoFixo)
admin.site.register(Datas)
