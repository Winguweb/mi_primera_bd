from .models import Organizacion, Cuenta, Contacto, Voluntario, Donante, CampoSexo

from django import forms
from django.forms import ModelForm, CheckboxInput
from django.forms.models import inlineformset_factory

from django_select2.forms import Select2Widget

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactoCrearForm(ModelForm):
    donanteCheckBox = forms.BooleanField(required=False, label='Donante', widget=CheckboxInput(attrs={'id': 'checkDonante',}))
    voluntarioCheckBox = forms.BooleanField(required=False, label='Voluntario', widget=CheckboxInput(attrs={'id': 'checkVoluntario',}))

    class Meta:
        model = Contacto
        fields = '__all__'


        widgets = {
            'cuenta': Select2Widget(attrs={'data-placeholder':"Crear cuenta nueva"}),
            'fecha_de_nacimiento': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(ContactoCrearForm, self).__init__(*args, **kwargs)
        self.fields['cuenta'].empty_label = "Crear cuenta automáticamente"
        self.fields['cuenta'].widget.choices = self.fields['cuenta'].choices
        
class DonanteCrearForm(ModelForm):
    class Meta:
        model = Donante
        exclude=['contacto']

class VoluntarioCrearForm(ModelForm):
    class Meta:
        model = Voluntario
        exclude=['contacto']