from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy
from .models import Organizacion, Cuenta, Contacto, Voluntario, Donante
from djmoney.forms.fields import MoneyField
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

CSV_CUENTA_INDEX = 0
CSV_NOMBRE_INDEX = 1
CSV_APELLIDO_INDEX = 2
CSV_TIPO_INDEX = 3
CSV_EMAIL_INDEX = 4
CSV_SEXO_INDEX = 5
CSV_TELEFONO_INDEX = 6


# Lista de cuentas
class CuentasLista(ListView): 
    model = Cuenta 
    context_object_name = 'mis_cuentas'  
    template_name = 'crm/cuentas_lista.html'

    def get_queryset(self):
        user = self.request.user
        listado_cuentas = Cuenta.objects.filter(organizacion__usuario=user).values_list('id', flat=True)

        query = self.request.GET.get('query')
        
        if query:
            return Cuenta.objects.filter(id__in=listado_cuentas).filter(Q(nombre__icontains=query))

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


DonanteFormSet = inlineformset_factory(Contacto, Donante, form=DonanteCrearForm, extra=1, max_num=1)
VoluntarioFormSet = inlineformset_factory(Contacto, Voluntario, form=VoluntarioCrearForm, extra=1, max_num=1)

class ContactoCrear(CreateView): 
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')


    def get_context_data(self, **kwargs):
        data = super(ContactoCrear, self).get_context_data(**kwargs)

        #filtro los sexos segun org
        data['form'].fields['sexo'].queryset = CampoSexo.objects.filter(organizacion__usuario=self.request.user)

        data['accion'] = 'Nuevo Contacto'
        if self.request.POST:
            data['donante'] = DonanteFormSet(self.request.POST)
            data['voluntario'] = VoluntarioFormSet(self.request.POST)
        else:
            data['donante'] = DonanteFormSet()
            data['voluntario'] = VoluntarioFormSet()
        return data

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        context = self.get_context_data()
        donante = context['donante']
        voluntario = context['voluntario']

        cuenta_nombre = form.cleaned_data['cuenta']
        if cuenta_nombre:
            cuenta = Cuenta.objects.filter(nombre__icontains=cuenta_nombre).filter(organizacion=organizacion)[:1].get()
        else:
            cuenta = Cuenta(organizacion=organizacion,nombre="Cuenta " + form.cleaned_data['apellido'], email=form.cleaned_data['email'])
            cuenta.save()

        
        form.instance.cuenta = cuenta
        self.object = form.save()

        es_donante = self.request.POST.get("donanteCheckBox", False)
        es_voluntario = self.request.POST.get("voluntarioCheckBox", False)

        if es_donante and not es_voluntario and donante.is_valid():
            form.instance.tipo = 1
            donante.instance = self.object
            donante.save()
        elif es_voluntario and not es_donante and voluntario.is_valid():
            form.instance.tipo = 2
            voluntario.instance = self.object
            voluntario.save()
        elif es_donante and es_voluntario and donante.is_valid() and voluntario.is_valid():
            form.instance.tipo = 3
            donante.instance = self.object
            donante.save()
            voluntario.instance = self.object
            voluntario.save()
        else:
            form.instance.tipo = 0

        self.object = form.save()
        return super(ContactoCrear, self).form_valid(form)

class ContactoEditar(UpdateView): 
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crm/creacion_contacto.html'
    success_url = reverse_lazy('contactos')


    def get_context_data(self, **kwargs):
        data = super(ContactoEditar, self).get_context_data(**kwargs)
        data['accion'] = 'Editar Contacto'

        #filtro los sexos segun org
        data['form'].fields['sexo'].queryset = CampoSexo.objects.filter(organizacion__usuario=self.request.user)

        if self.request.POST:
            data['donante'] = DonanteFormSet(self.request.POST, instance=self.object)
            data['voluntario'] = VoluntarioFormSet(self.request.POST, instance=self.object)
        else:
            data['donante'] = DonanteFormSet(instance=self.object)
            data['voluntario'] = VoluntarioFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        user = self.request.user
        organizacion = Organizacion.objects.filter(usuario=user)[:1].get()

        context = self.get_context_data()
        donante = context['donante']
        voluntario = context['voluntario']

        cuenta_nombre = form.cleaned_data['cuenta']
        if cuenta_nombre:
            cuenta = Cuenta.objects.filter(nombre=cuenta_nombre)[:1].get()
        else:
            cuenta = Cuenta(organizacion=organizacion,nombre="Cuenta " + form.cleaned_data['apellido'])
            cuenta.save()
        
        form.instance.cuenta = cuenta
        self.object = form.save()

        es_donante = self.request.POST.get("donanteCheckBox", False)
        es_voluntario = self.request.POST.get("voluntarioCheckBox", False)

        if es_donante and not es_voluntario and donante.is_valid():
            form.instance.tipo = 1
            donante.instance = self.object
            donante.save()
        elif es_voluntario and not es_donante and voluntario.is_valid():
            form.instance.tipo = 2
            voluntario.instance = self.object
            voluntario.save()
        elif es_donante and es_voluntario and donante.is_valid() and voluntario.is_valid():
            form.instance.tipo = 3
            donante.instance = self.object
            donante.save()
            voluntario.instance = self.object
            voluntario.save()
        else:
            form.instance.tipo = 0

        self.object = form.save()
        return super(ContactoEditar, self).form_valid(form)






class DashBoard(ListView):
    model = Contacto
    context_object_name = 'metricas'
    template_name = 'crm/dashboard.html'

    def get_queryset(self):
        user = self.request.user
        listado_contactos = Contacto.objects.filter(cuenta__organizacion__usuario=user).values_list('id', flat=True)
        cantidad_contactos = Contacto.objects.filter(id__in=listado_contactos).count()
        return cantidad_contactos

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

    for linea in lineas:                      
        try:
            fields = linea.split(",")
            id_cuenta = fields[CSV_CUENTA_INDEX]
            cuenta = Cuenta.objects.get(id=id_cuenta)

            nombre = fields[CSV_NOMBRE_INDEX]
            apellido = fields[CSV_APELLIDO_INDEX]
            tipo = int(fields[CSV_TIPO_INDEX])
            email = fields[CSV_EMAIL_INDEX]
            sexo = int(fields[CSV_SEXO_INDEX])
            telefono = fields[CSV_TELEFONO_INDEX]
            
            contacto = Contacto(cuenta=cuenta, nombre=nombre, 
                apellido=apellido, tipo=tipo, email=email,
                 sexo=sexo, telefono=telefono)
            contacto.save()              
        except Exception as e:
            print("Error cargando un usuario: " + linea)
            print(e)
    return HttpResponseRedirect(reverse("contactos"))


# Lista de cuentas
class CamposCustom(TemplateView):
    template_name = 'crm/custom.html'
    context_object_name = 'campos'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(CamposCustom, self).get_context_data(**kwargs)
        context['camposexo'] = CampoSexo.objects.filter(organizacion__usuario=user)
        print(context['camposexo'])
        #context['modeltwo'] = ModelTwo.objects.get(*query logic*)
        return context


