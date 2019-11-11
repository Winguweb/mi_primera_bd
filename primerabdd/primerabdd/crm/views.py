from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy
from .models import Organizacion, Cuenta, Contacto, Voluntario, CampoCustomOrigen, CampoCustomTipoContacto, CampoCustomTipoCuenta, Oportunidad, CampoCustomTipoOportunidad, CampoCustomEstadoOportunidad
from djmoney.forms.fields import MoneyField
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms.models import inlineformset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_date
from django.db import IntegrityError

from django.db import models
from django.db.models.deletion import ProtectedError
from django.template import loader
from django.db.models import Count

import sweetify


CSV_NOMBRE_INDEX = 0
CSV_APELLIDO_INDEX = 1
CSV_DOCUMENTO_INDEX = 2
CSV_CARGO_INDEX = 3
CSV_OCUPACION_INDEX = 4
CSV_CALLE_INDEX = 5
CSV_NUMERO_INDEX = 6
CSV_CIUDAD_INDEX = 7
CSV_COD_POSTAL_INDEX = 8
CSV_PAIS_INDEX = 9
CSV_FECHA_NACIMIENTO_INDEX = 10
CSV_TIPO_INDEX = 11
CSV_EMAIL_INDEX = 12
CSV_EMAIL_ALTERNATIVO_INDEX = 13 
CSV_TELEFONO_INDEX = 14
CSV_MOVIL_INDEX = 15
CSV_RECIBIR_NOVEDADES_INDEX = 16
CSV_OBSERVACIONES_INDEX = 17
CSV_ES_VOLUNTARIO_INDEX = 18
CSV_TURNO_INDEX = 19
CSV_ESTADO_INDEX = 20
CSV_HABILIDADES_INDEX = 21
CSV_CATEGORIA_INDEX = 22
CSV_NOMBRE_CUENTA_INDEX = 23
CSV_NOMBRE_ORIGEN_INDEX = 24
CSV_GENERO_INDEX = 25

# Lista de cuentas
class CuentasLista(ListView): 
    model = Cuenta 
    context_object_name = 'mis_cuentas'  
    template_name = 'crm/cuentas_lista.html'

    def get_queryset(self):
        user = self.request.user
        id_listado_cuentas = Cuenta.objects.filter(organizacion__usuario=user).values_list('id', flat=True)

        query = self.request.GET.get('query')

        listado_cuentas = Cuenta.objects.filter(id__in=id_listado_cuentas)
        
        if query:
            listado_cuentas = Cuenta.objects.filter(id__in=listado_cuentas).filter(Q(nombre__icontains=query))

        for cuenta_actual in listado_cuentas:
            #Tomo lps Contactos segun cuenta
            contactos = Contacto.objects.filter(cuenta__id=cuenta_actual.id).values_list('id', flat=True)
            if not contactos:
                cuenta_actual.tiene_contactos = True
            else:
                cuenta_actual.tiene_contactos = False

        paginator = Paginator(listado_cuentas,10)
        page = self.request.GET.get('page')
        listado_cuentas_paginado = paginator.get_page(page) 
        listado_cuentas_paginado.query = query
        return listado_cuentas_paginado

class CuentasDetalles(DetailView): 
    model = Cuenta
    context_object_name = 'cuenta'  
    template_name = 'crm/cuentas_detalles.html'

class CuentasEliminar(DeleteView): 
    model = Cuenta
    success_url = reverse_lazy('ver_cuentas')  

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CuentasCrear(CreateView):
    model = Cuenta
    form_class = CuentaCrearForm
    template_name = 'crm/creacion_cuenta.html'
    success_url = reverse_lazy('ver_cuentas')

    def get_form_kwargs(self):
        kwargs = super(CuentasCrear, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super(CuentasCrear, self).get_context_data(**kwargs)

        return data


    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        form.instance.organizacion = organizacion

        try:
            self.object = form.save()
        except IntegrityError as e:
            sweetify.error(self.request, 'Error', text='Ya existe una cuenta con este nombre.', persistent='Ok')
            return render(self.request, self.template_name, {'form': form})
        else:
            return super(CuentasCrear, self).form_valid(form)

    
class CuentasEditar(UpdateView): 
    model = Cuenta
    form_class = CuentaCrearForm
    template_name = 'crm/creacion_cuenta.html'
    success_url = reverse_lazy('ver_cuentas')

    def get_form_kwargs(self):
        kwargs = super(CuentasEditar, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super(CuentasEditar, self).get_context_data(**kwargs)

        return data

    def form_valid(self, form):
        try:
            self.object = form.save()
        except IntegrityError as e:
            sweetify.error(self.request, 'Error', text='Ya existe una cuenta con este nombre.', persistent='Ok')
            return render(self.request, self.template_name, {'form': form})
        else:
            return super(CuentasEditar, self).form_valid(form)
        


class CuentasContactos(TemplateView):
    context_object_name = 'contatos_cuenta'
    template_name = 'crm/cuentas_contactos.html'

    def get_context_data(self, **kwargs):

        cuenta_id = self.kwargs['pk']
        listado_contactos = Contacto.objects.filter(cuenta__id=cuenta_id).values_list('id', flat=True)       

        context = super(CuentasContactos, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        if query:
            listado_contactos = Contacto.objects.filter(Q(nombre__icontains=query) | 
            Q(apellido__icontains=query)).filter(id__in=listado_contactos)
        else:
            listado_contactos = Contacto.objects.filter(id__in=listado_contactos)

        paginator = Paginator(listado_contactos,10)
        page = self.request.GET.get('page')
        listado_contactos_paginado = paginator.get_page(page)     
        context['genericos'] = listado_contactos_paginado
        context['query'] = query

        return context

# Lista de contactos
class ContactosPorNivel(TemplateView): 
    context_object_name = 'mis_contactos'  
    template_name = 'crm/contactos_lista.html'  

    def get_context_data(self, **kwargs):

        user = self.request.user
        listado_contactos = Contacto.objects.filter(cuenta__organizacion__usuario=user).values_list('id', flat=True)       

        context = super(ContactosPorNivel, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        if query:
            listado_contactos = Contacto.objects.filter(Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | Q(cuenta__nombre__icontains=query)).filter(id__in=listado_contactos)
        else:
            listado_contactos = Contacto.objects.filter(id__in=listado_contactos)

        paginator = Paginator(listado_contactos,10)
        page = self.request.GET.get('page')
        listado_contactos_paginado = paginator.get_page(page)     
        context['genericos'] = listado_contactos_paginado
        context['query'] = query

        return context


class ContactoEliminar(DeleteView): 
    model = Contacto
    template_name = 'crm/confirmar_eliminacion.html'
    success_url = reverse_lazy('contactos')

class ContactoCrear(CreateView): 
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')

    def get_form_kwargs(self):
        kwargs = super(ContactoCrear, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super(ContactoCrear, self).get_context_data(**kwargs)    
        data['accion'] = 'Nuevo Contacto'

        return data

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        cuenta_nombre = form.cleaned_data['cuenta']
        if cuenta_nombre:
            cuenta = Cuenta.objects.filter(nombre__icontains=cuenta_nombre).filter(organizacion=organizacion)[:1].get()
        else:
            cuenta = Cuenta(organizacion=organizacion,nombre="Cuenta " + form.cleaned_data['apellido'], email=form.cleaned_data['email'])
            try:
                cuenta.save()
            except IntegrityError as e:
                sweetify.error(self.request, 'Error', text='Ya existe una cuenta con este apellido.\nPor favor cree la cuenta manualmente.', persistent='Ok')
                return render(self.request, self.template_name, {'form': form, 'accion': 'Nuevo Contacto'})
        
        form.instance.cuenta = cuenta    
        try:
            self.object = form.save()
        except IntegrityError as e:
            sweetify.error(self.request, 'Error', text='Ya existe un contacto con este mail en esta cuenta.', persistent='Ok')
            return render(self.request, self.template_name, {'form': form, 'accion': 'Nuevo Contacto'})
        else:
            return super(ContactoCrear, self).form_valid(form)

    def form_invalid(self, form):
        sweetify.error(self.request, 'Error', text='Ya existe un contacto con este mail en esta cuenta.', persistent='Ok')
        return render(self.request, self.template_name, {'form': form, 'accion': 'Nuevo Contacto'})

        

class ContactoDetalle(DetailView): 
    model = Contacto
    context_object_name = 'contacto'  
    template_name = 'crm/contacto_detalles.html'

class ContactoEditar(UpdateView): 
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')

    def get_form_kwargs(self):
        kwargs = super(ContactoEditar, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super(ContactoEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Contacto'

        return data

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        return qs

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        cuenta_nombre = form.cleaned_data['cuenta']
        if cuenta_nombre:
            cuenta = Cuenta.objects.filter(nombre=cuenta_nombre)[:1].get()
        else:
            cuenta = Cuenta(organizacion=organizacion,nombre="Cuenta " + form.cleaned_data['apellido'])
            try:
                cuenta.save()
            except IntegrityError as e:
                sweetify.error(self.request, 'Error', text='Ya existe una cuenta con este apellido.\nPor favor cree la cuenta manualmente.', persistent='Ok')
                return render(self.request, self.template_name, {'form': form, 'accion': 'Nuevo Contacto'})
        
        form.instance.cuenta = cuenta

        try:
            self.object = form.save()
        except IntegrityError as e:
            sweetify.error(self.request, 'Error', text='Ya existe un contacto con este mail en esta cuenta.', persistent='Ok')
            return render(self.request, self.template_name, {'form': form, 'accion': 'Nuevo Contacto'})
        else:
            return super(ContactoEditar, self).form_valid(form)


    def form_invalid(self, form):
        sweetify.error(self.request, 'Error', text='Ya existe un contacto con este mail en esta cuenta.', persistent='Ok')
        return render(self.request, self.template_name, {'form': form, 'accion': 'Editar Contacto'})



class DashBoard(ListView):
    model = Contacto
    context_object_name = 'metricas'
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashBoard, self).get_context_data(**kwargs)
        usuario = self.request.user

        # Cuentas con Oportunidades
        cuentas = Cuenta.objects.filter(organizacion__usuario=usuario)\
                                .annotate(cantidad_oportunidades=Count('oportunidad'))\
                                .filter(cantidad_oportunidades__gte=1)
        cantidad_cuentas_con_oportunidad = cuentas.count()
        context['cantidad_cuentas_con_oportunidad'] = cantidad_cuentas_con_oportunidad


        # Contactos por Tipo
        contactos_por_tipo = Contacto.objects.filter(cuenta__organizacion__usuario=usuario, categoria__tipo__isnull=False)\
                                            .values('categoria__tipo')\
                                            .annotate(total=Count('categoria'))\
                                            .order_by('categoria__tipo')
        context['contactos_por_tipo'] = contactos_por_tipo

        # Cuentas por Tipo
        cuentas_por_tipo = Cuenta.objects.filter(organizacion__usuario=usuario, tipo__tipo__isnull=False)\
                                        .values('tipo__tipo')\
                                        .annotate(total=Count('tipo'))\
                                        .order_by('tipo__tipo')
        context['cuentas_por_tipo'] = cuentas_por_tipo

        # Oportunidades por Estado
        oportunidades_por_estado = Oportunidad.objects.filter(cuenta__organizacion__usuario=usuario, estado_oportunidad__estado__isnull=False)\
                                                .values('estado_oportunidad__estado')\
                                                .annotate(total=Count('estado_oportunidad'))\
                                                .order_by('estado_oportunidad__estado')
        context['oportunidades_por_estado'] = oportunidades_por_estado

        return context

class Importador(TemplateView):

    template_name = 'crm/uploader.html'


def upload_csv(request):
    if "GET" == request.method:
        return HttpResponseRedirect(reverse("contactos"))

    user = request.user
    csv_file = request.FILES["csv_file"]

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'El archivo no es un csv')
        return HttpResponseRedirect(reverse("ver_importador"))
    if csv_file.multiple_chunks():
        messages.error(request,'El archivo es muy grande')
        return HttpResponseRedirect(reverse("ver_importador"))

    file_data = csv_file.read().decode("utf-8")     
    lineas = file_data.split("\n")
    total_contacts = 0
    failed_contacts = 0

    for linea in lineas:
        total_contacts +=1                      
        try:
            fields = linea.split(",")

            nombre = fields[CSV_NOMBRE_INDEX]
            apellido = fields[CSV_APELLIDO_INDEX]
            documento = fields[CSV_DOCUMENTO_INDEX]
            cargo = fields[CSV_CARGO_INDEX]
            ocupacion = fields[CSV_OCUPACION_INDEX]
            calle = fields[CSV_CALLE_INDEX]
            numero = fields[CSV_NUMERO_INDEX]
            ciudad = fields[CSV_CIUDAD_INDEX]
            cod_postal = fields[CSV_COD_POSTAL_INDEX]
            pais = fields[CSV_PAIS_INDEX]
            fecha_nacimiento = fields[CSV_FECHA_NACIMIENTO_INDEX]

            tipo = fields[CSV_TIPO_INDEX]
            email = fields[CSV_EMAIL_INDEX]
            email_alternativo = fields[CSV_EMAIL_ALTERNATIVO_INDEX]
            telefono = fields[CSV_TELEFONO_INDEX]
            movil = fields[CSV_MOVIL_INDEX]
            recibir_novedades = fields[CSV_RECIBIR_NOVEDADES_INDEX]
            observaciones = fields[CSV_OBSERVACIONES_INDEX]
            es_voluntario = fields[CSV_ES_VOLUNTARIO_INDEX]

            turno = fields[CSV_TURNO_INDEX]
            estado = fields[CSV_ESTADO_INDEX]
            habilidades = fields[CSV_HABILIDADES_INDEX]
            categoria = fields[CSV_CATEGORIA_INDEX]
            nombre_cuenta = fields[CSV_NOMBRE_CUENTA_INDEX]
            origen = fields[CSV_NOMBRE_ORIGEN_INDEX]
            sexo = fields[CSV_GENERO_INDEX]
            
            id_listado_cuentas = Cuenta.objects.filter(organizacion__usuario=user).filter(nombre=nombre_cuenta).values_list('id', flat=True)
            print(id_listado_cuentas)
            cuenta = None
            if not id_listado_cuentas:
                cuenta = Cuenta.objects.create(organizacion=user.organizacion,nombre=nombre_cuenta,email=email_alternativo)
            else:
                cuenta = Cuenta.objects.filter(id=id_listado_cuentas[0])[0]


            tipoCustom = CampoCustomTipoContacto.objects.filter(organizacion__usuario=user).filter(tipo=tipo)
            if not tipoCustom:
                categoria = CampoCustomTipoContacto.objects.create(organizacion=user.organizacion,tipo=tipo)
            else:
                categoria = tipoCustom[0]
            
            campoOrigen = CampoCustomOrigen.objects.filter(organizacion__usuario=user).filter(origen=origen)
            if not campoOrigen:
                origen = CampoCustomOrigen.objects.create(organizacion=user.organizacion,origen=origen)
            else:
                origen = campoOrigen[0]

            if turno == "Mañana":
                turno = 0
            else:
                turno = 1
            if estado == "Activo":
                estado = 1
            else: 
                estado = 0           
            contacto = Contacto(cuenta=cuenta, nombre=nombre, 
                apellido=apellido, email=email, tipo=0, categoria=categoria, documento=documento,
                cargo=cargo, ocupacion=ocupacion, direccion=calle + " " + numero, ciudad=ciudad, 
                pais=pais,cod_postal=cod_postal, email_alternativo=email_alternativo, observaciones=observaciones,
                movil=movil,origen=origen, habilidades=3, turno=turno, estado=estado, es_voluntario=True,
                 sexo=sexo, telefono=telefono, fecha_de_nacimiento=parse_date(fecha_nacimiento))
            contacto.save()              
        except Exception as e:
            print("Error cargando un usuario: " + linea)
            print(e)
            failed_contacts += 1
    messages.error(request,"Se importaron {} de {} contactos".format(total_contacts - failed_contacts, total_contacts))
    return HttpResponseRedirect(reverse("contactos"))


# Lista de campos custom por organizacion
class CamposCustom(TemplateView):
    template_name = 'crm/custom.html'
    context_object_name = 'campos'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(CamposCustom, self).get_context_data(**kwargs)
        context['camposOrigen'] = CampoCustomOrigen.objects.filter(organizacion__usuario=user)
        context['camposTipoContacto'] = CampoCustomTipoContacto.objects.filter(organizacion__usuario=user)
        context['tiposCuenta'] = CampoCustomTipoCuenta.objects.filter(organizacion__usuario=user)
        context['estadosOportunidad'] = CampoCustomEstadoOportunidad.objects.filter(organizacion__usuario=user)
        context['tiposOportunidad'] = CampoCustomTipoOportunidad.objects.filter(organizacion__usuario=user)
        #context['modeltwo'] = ModelTwo.objects.get(*query logic*)
        return context

class CampoCustomOrigenCrear(CreateView):
    model = CampoCustomOrigen
    form_class = CampoCustomCrearOrigenForm
    template_name = 'crm/crear_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomOrigenCrear, self).get_context_data(**kwargs)
        data['accion'] = 'Agregar Campo Origen'

        return data
    
    def form_invalid(self, form):
        print(form.errors)
    
    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomOrigenCrear, self).form_valid(form)

class CampoCustomOrigenEditar(UpdateView):
    model = CampoCustomOrigen
    template_name = 'crm/crear_custom.html'
    form_class = CampoCustomCrearOrigenForm
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomOrigenEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Campo Origen'

        return data
    
    def form_invalid(self, form):
        print(form.errors)

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomOrigenEditar, self).form_valid(form)
    

class CampoCustomOrigenEliminar(DeleteView): 
    model = CampoCustomOrigen
    template_name = 'crm/eliminar_campo_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        context = super(CampoCustomOrigenEliminar, self).get_context_data(**kwargs)
        context["nombre"] = self.object
        return context

    def delete(self, request, *args, **kwargs):
        try:
            return super(CampoCustomOrigenEliminar, self).delete(
                request, *args, **kwargs
            )
        except models.ProtectedError as e:
            # Return the appropriate response
            sweetify.error(self.request, 'Error', text='Existen contactos usando este campo!', persistent='Ok')
            return HttpResponseRedirect(self.success_url)

class CampoCustomTipoContactoCrear(CreateView):
    model = CampoCustomTipoContacto
    form_class = CampoCustomCrearTipoContactoForm
    template_name = 'crm/crear_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomTipoContactoCrear, self).get_context_data(**kwargs)
        data['accion'] = 'Agregar Campo Tipo De Contacto'

        return data
    
    def form_invalid(self, form):
        print(form.errors)
    
    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        print(organizacion)
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomTipoContactoCrear, self).form_valid(form)

class CampoCustomTipoContactoEditar(UpdateView):
    model = CampoCustomTipoContacto
    template_name = 'crm/crear_custom.html'
    form_class = CampoCustomCrearTipoContactoForm
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomTipoContactoEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Campo Tipo de Contacto'

        return data
    
    def form_invalid(self, form):
        print(form.errors)

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomTipoContactoEditar, self).form_valid(form)

class CampoCustomTipoContactoEliminar(DeleteView): 
    model = CampoCustomTipoContacto
    template_name = 'crm/eliminar_campo_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        context = super(CampoCustomTipoContactoEliminar, self).get_context_data(**kwargs)
        context["nombre"] = self.object
        return context
    
    def delete(self, request, *args, **kwargs):
        try:
            return super(CampoCustomTipoContactoEliminar, self).delete(
                request, *args, **kwargs
            )
        except models.ProtectedError as e:
            # Return the appropriate response
            sweetify.error(self.request, 'Error', text='Existen contactos usando este campo!', persistent='Ok')
            return HttpResponseRedirect(self.success_url)

class CampoCustomTipoCuentaCrear(CreateView):
    model = CampoCustomTipoCuenta
    form_class = CampoCustomCrearTipoCuentaForm
    template_name = 'crm/crear_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomTipoCuentaCrear, self).get_context_data(**kwargs)
        data['accion'] = 'Agregar Campo Tipo De Cuenta'

        return data
    
    def form_invalid(self, form):
        print(form.errors)
    
    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomTipoCuentaCrear, self).form_valid(form)

class CampoCustomTipoCuentaEditar(UpdateView):
    model = CampoCustomTipoCuenta
    template_name = 'crm/crear_custom.html'
    form_class = CampoCustomCrearTipoCuentaForm
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomTipoCuentaEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Campo Tipo de Cuenta'

        return data
    
    def form_invalid(self, form):
        print(form.errors)

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomTipoCuentaEditar, self).form_valid(form)


class CampoCustomTipoCuentaEliminar(DeleteView): 
    model = CampoCustomTipoCuenta
    template_name = 'crm/eliminar_campo_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        context = super(CampoCustomTipoCuentaEliminar, self).get_context_data(**kwargs)
        context["nombre"] = self.object
        return context
    
    def delete(self, request, *args, **kwargs):
        try:
            return super(CampoCustomTipoCuentaEliminar, self).delete(
                request, *args, **kwargs
            )
        except models.ProtectedError as e:
            # Return the appropriate response
            sweetify.error(self.request, 'Error', text='Existen cuentas usando este campo!', persistent='Ok')
            return HttpResponseRedirect(self.success_url)

class CampoCustomEstadoOportunidadCrear(CreateView):
    model = CampoCustomEstadoOportunidad
    form_class = CampoCustomCrearEstadoOportunidadForm
    template_name = 'crm/crear_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomEstadoOportunidadCrear, self).get_context_data(**kwargs)
        data['accion'] = 'Agregar Campo Estado De Oportunidad'
        print(data['form'])
        return data
    
    def form_invalid(self, form):
        print(form.errors)
    
    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomEstadoOportunidadCrear, self).form_valid(form)

class CampoCustomEstadoOportunidadEditar(UpdateView):
    model = CampoCustomEstadoOportunidad
    template_name = 'crm/crear_custom.html'
    form_class = CampoCustomCrearEstadoOportunidadForm
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomEstadoOportunidadEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Campo Estado de Oportunidad'

        return data
    
    def form_invalid(self, form):
        print(form.errors)

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomEstadoOportunidadEditar, self).form_valid(form)


class CampoCustomEstadoOportunidadEliminar(DeleteView): 
    model = CampoCustomEstadoOportunidad
    template_name = 'crm/eliminar_campo_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        context = super(CampoCustomEstadoOportunidadEliminar, self).get_context_data(**kwargs)
        context["nombre"] = self.object
        return context

    def delete(self, request, *args, **kwargs):
        try:
            return super(CampoCustomEstadoOportunidadEliminar, self).delete(
                request, *args, **kwargs
            )
        except models.ProtectedError as e:
            # Return the appropriate response
            sweetify.error(self.request, 'Error', text='Existen oportunidades usando este campo!', persistent='Ok')
            return HttpResponseRedirect(self.success_url)

class CampoCustomTipoOportunidadCrear(CreateView):
    model = CampoCustomTipoOportunidad
    form_class = CampoCustomCrearTipoOportunidadForm
    template_name = 'crm/crear_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomTipoOportunidadCrear, self).get_context_data(**kwargs)
        data['accion'] = 'Agregar Campo Tipo De Oportunidad'

        return data
    
    def form_invalid(self, form):
        print(form.errors)
    
    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomTipoOportunidadCrear, self).form_valid(form)

class CampoCustomTipoOportunidadEditar(UpdateView):
    model = CampoCustomTipoOportunidad
    template_name = 'crm/crear_custom.html'
    form_class = CampoCustomCrearTipoOportunidadForm
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        data = super(CampoCustomTipoOportunidadEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Campo Tipo de Oportunidad'

        return data
    
    def form_invalid(self, form):
        print(form.errors)

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion

        self.object = form.save()
        return super(CampoCustomTipoOportunidadEditar, self).form_valid(form)


class CampoCustomTipoOportunidadEliminar(DeleteView): 
    model = CampoCustomTipoOportunidad
    template_name = 'crm/eliminar_campo_custom.html'
    success_url = reverse_lazy('campos_custom')

    def get_context_data(self, **kwargs):
        context = super(CampoCustomTipoOportunidadEliminar, self).get_context_data(**kwargs)
        context["nombre"] = self.object
        return context

    def delete(self, request, *args, **kwargs):
        try:
            return super(CampoCustomTipoOportunidadEliminar, self).delete(
                request, *args, **kwargs
            )
        except models.ProtectedError as e:
            # Return the appropriate response
            sweetify.error(self.request, 'Error', text='Existen oportunidades usando este campo!', persistent='Ok')
            return HttpResponseRedirect(self.success_url)


# Lista de Oportunidades
class OportunidadesLista(ListView): 
    model = Oportunidad 
    context_object_name = 'mis_oportunidades'  
    template_name = 'crm/oportunidades_lista.html'

    def get_queryset(self):
        user = self.request.user
        id_listado_cuentas = Cuenta.objects.filter(organizacion__usuario=user).values_list('id', flat=True)

        listado_oportunidades = Oportunidad.objects.filter(cuenta__id__in=id_listado_cuentas)
        return listado_oportunidades

class OportunidadesEditar(UpdateView): 
    model = Oportunidad
    form_class = OportunidadCrearForm
    template_name = 'crm/creacion_oportunidad.html'
    success_url = reverse_lazy('ver_oportunidades')

    def get_context_data(self, **kwargs):
        data = super(OportunidadesEditar, self).get_context_data(**kwargs)
        
        #Filtro los campos custom por organizacion
        tiposOportunidad_de_org = CampoCustomTipoOportunidad.objects.filter(organizacion__usuario=self.request.user)
        estadosOportunidad_de_org = CampoCustomEstadoOportunidad.objects.filter(organizacion__usuario=self.request.user)

        data['form'].fields['tipo'].queryset = tiposOportunidad_de_org
        data['form'].fields['estado_oportunidad'].queryset = estadosOportunidad_de_org

        return data

class OportunidadesCrear(CreateView):
    model = Oportunidad
    form_class = OportunidadCrearForm
    template_name = 'crm/creacion_oportunidad.html'
    success_url = reverse_lazy('ver_oportunidades')

    def get_context_data(self, **kwargs):
        data = super(OportunidadesCrear, self).get_context_data(**kwargs)
        
        #Filtro los campos custom por organizacion
        tiposOportunidad_de_org = CampoCustomTipoOportunidad.objects.filter(organizacion__usuario=self.request.user)
        estadosOportunidad_de_org = CampoCustomEstadoOportunidad.objects.filter(organizacion__usuario=self.request.user)

        data['form'].fields['tipo'].queryset = tiposOportunidad_de_org
        data['form'].fields['estado_oportunidad'].queryset = estadosOportunidad_de_org

        #filtro las cuentas segun org
        cuentas_de_la_organizacion = Cuenta.objects.filter(organizacion__usuario=self.request.user)
        data['form'].fields['cuenta'].queryset = cuentas_de_la_organizacion

        return data

class OportunidadesEliminar(DeleteView): 
    model = Oportunidad
    success_url = reverse_lazy('ver_oportunidades')  

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class OportunidadesDetalles(DetailView): 
    model = Oportunidad
    context_object_name = 'oportunidad'  
    template_name = 'crm/oportunidades_detalles.html'