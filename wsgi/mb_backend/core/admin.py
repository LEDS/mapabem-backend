from django.contrib import admin
from .models import Comunidade
from .models import Categoria
from negocio.models import Comercio
from cultura.models import ObraExposta, Artista, PontoReferenciaCultural


class ComercioAdmin(admin.ModelAdmin):
    model = Comercio
    list_display = ['nome', 'get_comunidade', ]

    def get_comunidade(self, obj):
        return obj.comunidade.nome
    get_comunidade.admin_order_field  = 'comunidade'  #Allows column order sorting
    get_comunidade.short_description = 'Comunidade'  #Renames column head

class ObraExpostaAdmin(admin.ModelAdmin):
    model = ObraExposta
    list_display = ['nome', 'get_comunidade', ]

    def get_comunidade(self, obj):
        return obj.comunidade.nome
    get_comunidade.admin_order_field  = 'comunidade'  #Allows column order sorting
    get_comunidade.short_description = 'Comunidade'  #Renames column head


class ArtistaAdmin(admin.ModelAdmin):
    model = Artista
    list_display = ['nome', 'get_comunidade', ]

    def get_comunidade(self, obj):
        return obj.comunidade.nome
    get_comunidade.admin_order_field  = 'comunidade'  #Allows column order sorting
    get_comunidade.short_description = 'Comunidade'  #Renames column head

class PontoReferenciaCulturalAdmin(admin.ModelAdmin):
    model = PontoReferenciaCultural
    list_display = ['nome', 'get_comunidade', ]

    def get_comunidade(self, obj):
        return obj.comunidade.nome
    get_comunidade.admin_order_field  = 'comunidade'  #Allows column order sorting
    get_comunidade.short_description = 'Comunidade'  #Renames column head


# Register your models here.
admin.site.register(Comunidade)
admin.site.register(Categoria)
admin.site.register(Comercio, ComercioAdmin)
admin.site.register(ObraExposta, ObraExpostaAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(PontoReferenciaCultural, PontoReferenciaCulturalAdmin)
