from .models import Organizacion, Cuenta, Contacto, Voluntario, Oportunidad, CampoCustomOrigen, CampoCustomTipoContacto, CampoCustomTipoCuenta, CampoCustomTipoOportunidad, CampoCustomEstadoOportunidad
from django import forms
from django.forms import ModelForm, CheckboxInput


from django_select2.forms import Select2Widget

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactoCrearForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


        widgets = {
            'cuenta': Select2Widget(attrs={'data-placeholder':"Vacío para crear cuenta nueva"}),
            'origen': Select2Widget(attrs={'data-placeholder':""}),
            'categoria': Select2Widget(attrs={'data-placeholder':""}),
            'sexo': Select2Widget(attrs={'data-placeholder':""}),
            'fecha_de_nacimiento': DateInput(),
            'estado': Select2Widget(attrs={'data-placeholder':"Estado"}),
            'turno': Select2Widget(attrs={'data-placeholder':"Turno"}),
            'habilidades': Select2Widget(attrs={'data-placeholder':"Habilidades"}),
            'pais': Select2Widget(attrs={'data-placeholder':"Pais"}),

        }

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('user')
        super(ContactoCrearForm, self).__init__(*args, **kwargs)
        if self.current_user:
            #filtro los origenes segun org
            origenes_de_la_organizacion = CampoCustomOrigen.objects.filter(organizacion__usuario=self.current_user)
            self.fields['origen'].queryset = origenes_de_la_organizacion

            #filtro los tipos de contacto segun org
            tipos_de_contacto_de_la_organizacion = CampoCustomTipoContacto.objects.filter(organizacion__usuario=self.current_user)
            self.fields['categoria'].queryset = tipos_de_contacto_de_la_organizacion

            #filtro las cuentas segun org
            cuentas_de_la_organizacion = Cuenta.objects.filter(organizacion__usuario=self.current_user)
            self.fields['cuenta'].queryset = cuentas_de_la_organizacion


class CuentaCrearForm(ModelForm):
    class Meta:
        model = Cuenta
        exclude = ['organizacion']

        widgets = {
            'tipo': Select2Widget(attrs={'data-placeholder':""}),
        }

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('user')
        super(CuentaCrearForm, self).__init__(*args, **kwargs)
        if self.current_user:
            #Filtro los campos custom de tipo de cuenta por organizacion
            tiposCuenta_de_org = CampoCustomTipoCuenta.objects.filter(organizacion__usuario=self.current_user)
            self.fields['tipo'].queryset = tiposCuenta_de_org


class OportunidadCrearForm(ModelForm):
    class Meta:
        model = Oportunidad
        fields = '__all__'

        widgets = {
            'tipo': Select2Widget(attrs={'data-placeholder':"Tipo"}),
            'estado_oportunidad': Select2Widget(attrs={'data-placeholder':"Estado"}),
            'cuenta': Select2Widget(attrs={'data-placeholder':"Cuenta"}),
            'fecha': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(OportunidadCrearForm, self).__init__(*args, **kwargs)

class CampoCustomCrearOrigenForm(ModelForm):
    class Meta:
        model = CampoCustomOrigen
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearOrigenForm, self).__init__(*args, **kwargs)

class CampoCustomCrearTipoContactoForm(ModelForm):
    class Meta:
        model = CampoCustomTipoContacto
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearTipoContactoForm, self).__init__(*args, **kwargs)

class CampoCustomCrearTipoCuentaForm(ModelForm):
    class Meta:
        model = CampoCustomTipoCuenta
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearTipoCuentaForm, self).__init__(*args, **kwargs)

class CampoCustomCrearEstadoOportunidadForm(ModelForm):
    class Meta:
        model = CampoCustomEstadoOportunidad
        exclude = ['organizacion']

        widgets={
            'estado': forms.TextInput(attrs={'id': 'estado_custom_oportunidad'})
        }
        

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearEstadoOportunidadForm, self).__init__(*args, **kwargs)

class CampoCustomCrearTipoOportunidadForm(ModelForm):
    class Meta:
        model = CampoCustomTipoOportunidad
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearTipoOportunidadForm, self).__init__(*args, **kwargs)



