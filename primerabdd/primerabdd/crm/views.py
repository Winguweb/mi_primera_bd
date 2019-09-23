from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.urls import reverse_lazy
from .models import Organizacion, Cuenta, Contacto, Voluntario, Donante
from djmoney.forms.fields import MoneyField



# Lista de cuentas
class CuentasLista(ListView): 
    model = Cuenta 
    context_object_name = 'mis_cuentas'  
    template_name = 'crm/cuentas_lista.html'  

    def get_queryset(self):
        user = self.request.user
        listado_cuentas = Cuenta.objects.filter(organizacion__usuario=user).values_list('id', flat=True)

        return Cuenta.objects.filter(id__in=listado_cuentas)

class CuentasDetalles(DetailView): 
    model = Cuenta
    context_object_name = 'cuenta'  
    template_name = 'crm/cuentas_detalles.html'  






# Lista de contactos
class ContactosPorNivel(TemplateView): 
    context_object_name = 'mis_contactos'  
    template_name = 'crm/contactos_lista.html'  

    def get_context_data(self, **kwargs):

        user = self.request.user
        listado_contactos = Contacto.objects.filter(organizacion__usuario=user).values_list('id', flat=True)       

        context = super(ContactosPorNivel, self).get_context_data(**kwargs)        
        context['genericos'] = Contacto.objects.filter(id__in=listado_contactos)

        return context


class ContactoEliminar(DeleteView): 
    model = Contacto
    template_name = 'crm/confirmar_eliminacion.html'
    success_url = reverse_lazy('contactos')

# Form especial para excluir organizacion
class ContactoCrearForm(ModelForm):
    
    class Meta:
        model = Contacto
        exclude = ['organizacion', 'tipo',]
        
class DonanteCrearForm(ModelForm):
    class Meta:
        model = Donante
        exclude=['contacto']

class VoluntarioCrearForm(ModelForm):
    class Meta:
        model = Voluntario
        exclude=['contacto']

DonanteFormSet = inlineformset_factory(Contacto, Donante, form=DonanteCrearForm, extra=1, max_num=1)
VoluntarioFormSet = inlineformset_factory(Contacto, Voluntario, form=VoluntarioCrearForm, extra=1, max_num=1)

class ContactoCrear(CreateView): 
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')

    def get_context_data(self, **kwargs):
        data = super(ContactoCrear, self).get_context_data(**kwargs)
        if self.request.POST:
            data['donante'] = DonanteFormSet(self.request.POST)
            data['voluntario'] = VoluntarioFormSet(self.request.POST)
        else:
            data['donante'] = DonanteFormSet()
            data['voluntario'] = VoluntarioFormSet()
        return data

    def form_valid(self, form):
        user = self.request.user

        context = self.get_context_data()
        donante = context['donante']
        voluntario = context['voluntario']

        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion
        self.object = form.save()

        if donante.is_valid() and voluntario.is_valid():
            donante.instance = self.object
            donante.save()
            voluntario.instance = self.object
            voluntario.save()

        return super(ContactoCrear, self).form_valid(form)

class ContactoEditar(UpdateView): 
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')

    def get_context_data(self, **kwargs):
        data = super(ContactoEditar, self).get_context_data(**kwargs)
        if self.request.POST:
            data['donante'] = DonanteFormSet(self.request.POST, instance=self.object)
            data['voluntario'] = VoluntarioFormSet(self.request.POST, instance=self.object)
        else:
            data['donante'] = DonanteFormSet(instance=self.object)
            data['voluntario'] = VoluntarioFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        user = self.request.user

        context = self.get_context_data()
        donante = context['donante']
        voluntario = context['voluntario']

        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()
        form.instance.organizacion = organizacion
        self.object = form.save()

        if donante.is_valid() and voluntario.is_valid():
            donante.instance = self.object
            donante.save()
            voluntario.instance = self.object
            voluntario.save()

        return super(ContactoEditar, self).form_valid(form)






class DashBoard(ListView):
    model = Contacto
    context_object_name = 'metricas'
    template_name = 'crm/dashboard.html'

    def get_queryset(self):
        user = self.request.user
        listado_contactos = Contacto.objects.filter(organizacion__usuario=user).values_list('id', flat=True)
        cantidad_contactos = Contacto.objects.filter(id__in=listado_contactos).count()
        return cantidad_contactos

        