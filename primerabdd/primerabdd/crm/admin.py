from django.contrib import admin
from .models import Organizacion, CampoCustomTipoOportunidad, CampoCustomEstadoOportunidad

@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    #model = Organizacion
    #exclude = ['tyc_leido']
    pass


admin.site.register(CampoCustomTipoOportunidad)
admin.site.register(CampoCustomEstadoOportunidad)


