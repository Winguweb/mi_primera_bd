from django.urls import path

from . import views

urlpatterns = [
    path('', views.CuentasLista.as_view()),
    path('<int:pk>/', views.CuentasDetalles.as_view(), name='cuentas_detalles'),
]