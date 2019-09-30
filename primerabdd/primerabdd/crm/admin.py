from django.contrib import admin
from .models import Cuenta, Contacto, Organizacion, Donante, Voluntario

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

admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Contacto, ContactoAdmin)

admin.site.register(Voluntario)
admin.site.register(Donante)
