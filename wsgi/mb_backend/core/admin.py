from django.contrib import admin
from .models import Bairro
from .models import Categoria
from negocio.models import Comercio
from cultura.models import ObraExposta, Artista, PontoReferenciaCultural


class ComercioAdmin(admin.ModelAdmin):
    model = Comercio
    list_display = ['nome', 'get_bairro', ]

    def get_bairro(self, obj):
        return obj.bairro.nome
    get_bairro.admin_order_field  = 'bairro'  #Allows column order sorting
    get_bairro.short_description = 'Bairro'  #Renames column head

class ObraExpostaAdmin(admin.ModelAdmin):
    model = ObraExposta
    list_display = ['nome', 'get_bairro', ]

    def get_bairro(self, obj):
        return obj.bairro.nome
    get_bairro.admin_order_field  = 'bairro'  #Allows column order sorting
    get_bairro.short_description = 'Bairro'  #Renames column head


class ArtistaAdmin(admin.ModelAdmin):
    model = Artista
    list_display = ['nome', 'get_bairro', ]

    def get_bairro(self, obj):
        return obj.bairro.nome
    get_bairro.admin_order_field  = 'bairro'  #Allows column order sorting
    get_bairro.short_description = 'Bairro'  #Renames column head

class PontoReferenciaCulturalAdmin(admin.ModelAdmin):
    model = PontoReferenciaCultural
    list_display = ['nome', 'get_bairro', ]

    def get_bairro(self, obj):
        return obj.bairro.nome
    get_bairro.admin_order_field  = 'bairro'  #Allows column order sorting
    get_bairro.short_description = 'Bairro'  #Renames column head


# Register your models here.
admin.site.register(Bairro)
admin.site.register(Categoria)
admin.site.register(Comercio, ComercioAdmin)
admin.site.register(ObraExposta, ObraExpostaAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(PontoReferenciaCultural, PontoReferenciaCulturalAdmin)
