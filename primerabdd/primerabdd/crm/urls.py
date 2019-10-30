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
    path('custom/createOrigin/', views.CampoCustomOrigenCrear.as_view(), name='crear_custom_origen'),
    path('custom/editOrigin/<int:pk>', views.CampoCustomOrigenEditar.as_view(), name='editar_custom_origen'),
    path('custom/deleteOrigin/<int:pk>', views.CampoCustomOrigenEliminar.as_view(), name='eliminar_custom_origen'),
    path('custom/createContactType/', views.CampoCustomTipoContactoCrear.as_view(), name='crear_custom_tipo_contacto'),
    path('custom/editContactType/<int:pk>', views.CampoCustomTipoContactoEditar.as_view(), name='editar_custom_tipo_contacto'),
    path('custom/deleteContactType/<int:pk>', views.CampoCustomTipoContactoEliminar.as_view(), name='eliminar_custom_tipo_contacto'),
    path('custom/createAccountType/', views.CampoCustomTipoCuentaCrear.as_view(), name='crear_custom_tipo_cuenta'),
    path('custom/editAccountType/<int:pk>', views.CampoCustomTipoCuentaEditar.as_view(), name='editar_custom_tipo_cuenta'),
    path('custom/deleteAccountType/<int:pk>', views.CampoCustomTipoCuentaEliminar.as_view(), name='eliminar_custom_tipo_cuenta'),
    path('cuentas/create/', views.CuentasCrear.as_view(), name='crear_cuenta'),
    path('cuentas/edit/<int:pk>', views.CuentasEditar.as_view(), name='editar_cuenta'),
    path('cuentas/delete/<int:pk>', views.CuentasEliminar.as_view(), name='eliminar_cuenta'),
    path('oportunidades/', views.OportunidadesLista.as_view(), name='ver_oportunidades'),
]