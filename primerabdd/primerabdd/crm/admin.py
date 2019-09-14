from django.contrib import admin
from .models import Cuenta, Contacto, Organizacion

class ContactoInline(admin.TabularInline):
	model = Contacto


class CuentaInline(admin.TabularInline):
	model = Cuenta

class OrganizacionAdmin(admin.ModelAdmin):
	inlines = [
		CuentaInline,
		ContactoInline
	]

admin.site.register(Cuenta)
admin.site.register(Contacto)
admin.site.register(Organizacion, OrganizacionAdmin)
