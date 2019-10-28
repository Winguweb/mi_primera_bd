from .models import Organizacion, Cuenta, Contacto, Voluntario, CampoCustomOrigen, CampoCustomTipoContacto, CampoCustomTipoCuenta
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
        }

    def __init__(self, *args, **kwargs):
        super(ContactoCrearForm, self).__init__(*args, **kwargs)

class CuentaCrearForm(ModelForm):
    class Meta:
        model = Cuenta
        exclude = ['organizacion']

        widgets = {
            'tipo': Select2Widget(attrs={'data-placeholder':""}),
        }

    def __init__(self, *args, **kwargs):
        super(CuentaCrearForm, self).__init__(*args, **kwargs)

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