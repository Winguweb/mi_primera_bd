from django.contrib import admin
from .models import Cuenta, Contacto, Organizacion, Donante, Voluntario, CampoCustomGenero, CampoCustomOrigen, CampoCustomTipoContacto, CampoCustomTipoCuenta

class ContactoInline(admin.TabularInline):
    model = Contacto

class CuentaAdmin(admin.ModelAdmin):
    inlines = [
        ContactoInline
    ]   

class CuentaInline(admin.TabularInline):
    model = Cuenta

class OrganizacionAdmin(admin.ModelAdmin):
    inlines = [
        CuentaInline
    ]

class DonanteInline(admin.TabularInline):
    model = Donante

class VoluntarioInline(admin.TabularInline):
    model = Voluntario

class ContactoAdmin(admin.ModelAdmin):
    inlines = [
        DonanteInline,
        VoluntarioInline
    ]

admin.site.register(Organizacion)
admin.site.register(CampoCustomGenero)
admin.site.register(CampoCustomOrigen)
admin.site.register(CampoCustomTipoContacto)
admin.site.register(CampoCustomTipoCuenta)

