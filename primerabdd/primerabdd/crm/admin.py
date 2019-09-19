from django.contrib import admin
from .models import Cuenta, Contacto, Organizacion, Donante, Voluntario

class ContactoInline(admin.TabularInline):
	model = Contacto


class CuentaInline(admin.TabularInline):
	model = Cuenta

class OrganizacionAdmin(admin.ModelAdmin):
	inlines = [
		CuentaInline,
		ContactoInline
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
admin.site.register(Contacto, ContactoAdmin)

admin.site.register(Cuenta)
admin.site.register(Voluntario)
admin.site.register(Donante)
