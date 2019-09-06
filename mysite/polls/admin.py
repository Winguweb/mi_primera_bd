from django.contrib import admin

from .models import Cuenta, Contacto

class ContactoInline(admin.TabularInline):
	model = Contacto

class CuentaAdmin(admin.ModelAdmin):
	inlines = [
		ContactoInline
	]

admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Contacto)