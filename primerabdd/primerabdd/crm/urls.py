from django.urls import path

from . import views

urlpatterns = [
    path('cuentas/', views.CuentasLista.as_view(), name='ver_cuentas'),
    path('contactos/', views.ContactosPorNivel.as_view(), name='contactos'),
    path('cuentas/<int:pk>/contactos/', views.CuentasContactos.as_view(), name='cuentas_contactos'),
    path('cuentas/<int:pk>', views.CuentasDetalles.as_view(), name='cuentas_detalles'),
    path('delete/<int:pk>', views.ContactoEliminar.as_view(), name='eliminar_contacto'),
    path('create/', views.ContactoCrear.as_view(), name='crear_contacto'),
    path('contacto/<int:pk>/', views.ContactoDetalle.as_view(), name='contacto_detalle'),
    path('edit/<int:pk>', views.ContactoEditar.as_view(), name='editar_contacto'),
    path('dashboard/', views.DashBoard.as_view(),name='ver_dashboard'),
    path('carga/', views.Importador.as_view(),name='ver_importador'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),  
    path('custom/', views.CamposCustom.as_view(), name='campos_custom'),
    path('custom/deleteGender/<int:pk>', views.CampoCustomGeneroEliminar.as_view(), name='eliminar_custom_genero'),
    path('custom/deleteOrigin/<int:pk>', views.CampoCustomOrigenEliminar.as_view(), name='eliminar_custom_origen'),
    path('custom/deleteContactType/<int:pk>', views.CampoCustomTipoContactoEliminar.as_view(), name='eliminar_custom_tipo_contacto'),
    path('custom/deleteAccountType/<int:pk>', views.CampoCustomtipoCuentaEliminar.as_view(), name='eliminar_custom_tipo_cuenta'),
    path('cuentas/create/', views.CuentasCrear.as_view(), name='crear_cuenta'),
    path('cuentas/edit/<int:pk>', views.CuentasEditar.as_view(), name='editar_cuenta'),
]