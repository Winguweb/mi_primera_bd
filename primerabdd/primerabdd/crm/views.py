from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cuenta, Contacto


# Create your views here.
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

# class ContactCreate(CreateView): 
#     model = Contact

# class ContactUpdate(UpdateView): 
#     model = Contact

# class ContactDelete(DeleteView): 
#     model = Contact