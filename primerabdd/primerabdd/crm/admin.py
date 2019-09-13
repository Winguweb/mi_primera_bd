from django.contrib import admin
from .models import Cuenta, Contacto, Organizacion

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

admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Contacto)
admin.site.register(Organizacion, OrganizacionAdmin)
