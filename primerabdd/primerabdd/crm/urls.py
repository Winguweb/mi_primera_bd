from django.urls import path

from . import views

urlpatterns = [
    path('cuentas/', views.CuentasLista.as_view()),
    path('contactos/', views.ContactosLista.as_view()),
    path('cuentas/<int:pk>/', views.CuentasDetalles.as_view(), name='cuentas_detalles'),
]