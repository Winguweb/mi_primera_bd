from django.urls import path

from . import views

urlpatterns = [
    path('cuentas/', views.CuentasLista.as_view()),
    path('contactos/', views.ContactosLista.as_view(), name='contactos'),
    path('cuentas/<int:pk>/', views.CuentasDetalles.as_view(), name='cuentas_detalles'),
    path('delete/<int:pk>', views.ContactoEliminar.as_view(), name='eliminar_contacto'),
    path('create/', views.ContactoCrear.as_view(), name='crear_contacto'),
]