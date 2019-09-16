from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cuenta, Contacto, Voluntario, Donante


# Lista de cuentas
class CuentasLista(ListView): 
    model = Cuenta 
    context_object_name = 'mis_cuentas'  
    template_name = 'crm/cuentas_lista.html'  

    def get_queryset(self):
        user = self.request.user
        listado_cuentas = Cuenta.objects.filter(organizacion__usuario=user).values_list('id', flat=True)

        return Cuenta.objects.filter(id__in=listado_cuentas)

# Lista de contactos
class ContactosLista(ListView): 
    model = Contacto 
    context_object_name = 'mis_contactos'  
    template_name = 'crm/contactos_lista.html'  

    def get_queryset(self):
        user = self.request.user
        listado_contactos = Contacto.objects.filter(organizacion__usuario=user).values_list('id', flat=True)

        return Contacto.objects.filter(id__in=listado_contactos)

class ContactosPorNivel(TemplateView): 
    context_object_name = 'mis_contactos'  
    template_name = 'crm/contactos_lista.html'  

    def get_context_data(self, **kwargs):

        user = self.request.user
        listado_contactos = Contacto.objects.filter(organizacion__usuario=user).values_list('id', flat=True)
        listado_voluntarios = Voluntario.objects.filter(organizacion__usuario=user).values_list('id', flat=True)
        listado_donantes = Donante.objects.filter(organizacion__usuario=user).values_list('id', flat=True)
       

        context = super(ContactosPorNivel, self).get_context_data(**kwargs)        
        context['genericos'] = Contacto.objects.filter(id__in=listado_contactos).exclude(id__in=listado_voluntarios).exclude(id__in=listado_donantes)
        context['voluntarios'] = Voluntario.objects.filter(id__in=listado_voluntarios)
        context['donantes'] = Donante.objects.filter(id__in=listado_donantes)

        return context

class CuentasDetalles(DetailView): 
    model = Cuenta
    context_object_name = 'cuenta'  
    template_name = 'crm/cuentas_detalles.html'  

class ContactoEliminar(DeleteView): 
    model = Contacto
    template_name = 'crm/confirmar_eliminacion.html'
    success_url = reverse_lazy('contactos')

class ContactoCrear(CreateView): 
    model = Contacto
    fields = '__all__'
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')

class ContactoEditar(UpdateView): 
    model = Contacto
    fields = ('nombre', 'email', 'direccion', 'telefono',)
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')

class DashBoard(ListView):
    model = Contacto
    context_object_name = 'metricas'
    template_name = 'crm/dashboard.html'

    def get_queryset(self):
        user = self.request.user
        listado_contactos = Contacto.objects.filter(organizacion__usuario=user).values_list('id', flat=True)
        cantidad_contactos = Contacto.objects.filter(id__in=listado_contactos).count()
        return cantidad_contactos
    

# class ContactCreate(CreateView): 
#     model = Contact

# class ContactUpdate(UpdateView): 
#     model = Contact

# class ContactDelete(DeleteView): 
#     model = Contact