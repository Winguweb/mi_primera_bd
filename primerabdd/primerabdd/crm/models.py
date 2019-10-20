from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from djmoney.models.fields import MoneyField
from enum import Enum




class Organizacion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    fecha_alta = models.DateField('fecha de alta')

    

    class Meta:
        verbose_name_plural = 'organizaciones'

    def __str__(self):
        return self.nombre

#####################################################
###########     CAMPOS CUSTOMIZABLES    #############
#####################################################
class TiposCamposCustom(Enum):
    GENERO_CONTACTO = 1
    TIPO_CONTACTO = 2
    ORIGEN_CONTACTO = 3
    TIPO_CUENTA = 4
    ESTADO_OPORTUNIDADES = 5
    TIPO_OPORTUNIDADES = 6 

class CamposCustomOrganizacion(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    tipo_campo = models.PositiveIntegerField(blank=False, null=False)
    valor = models.CharField(max_length=50, default=None, blank=True, null=True)
    #sexo = models.CharField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return (self.valor) 

#####################################################
###########     CAMPOS CUSTOMIZABLES    #############
#####################################################      

class Cuenta(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, default=None, blank=False, null=False)

    calle = models.CharField(max_length=200 ,default=None, blank=True, null=True)
    numero = models.CharField(max_length=10, default=None, blank=True, null=True)
    ciudad = models.CharField(max_length=200, default=None, blank=True, null=True)
    cod_postal = models.CharField(max_length=10, default=None, blank=True, null=True)
    pais = models.CharField(max_length=200, default=None, blank=True, null=True)

    email = models.EmailField(default=None, blank=False, null=False)
    email_alternativo = models.EmailField(default=None, blank=True, null=True)

    tipo = models.OneToOneField(
            CamposCustomOrganizacion,
            related_name='tipo_de_cuenta',
            on_delete=models.CASCADE,
            blank=True,
            null=True
        )

    telefono = models.CharField(max_length=50, default=None, blank=True, null=True)
    telefono_alternativo = models.CharField(max_length=50, default=None, blank=True, null=True)
    
    web = models.CharField(max_length=200, default=None, blank=True, null=True)

    observaciones = models.TextField(default= None, blank=True, null=True)
    
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, blank=True)

    nombre = models.CharField(max_length=200, default=None, blank=False, null=False)

    apellido = models.CharField(max_length=200, default=None, blank=False, null=False)

    documento = models.CharField(max_length=10, default=None, blank=True, null=True)

    cargo = models.CharField(max_length=200, default=None, blank=True, null=True)

    ocupacion = models.CharField(max_length=200, default=None, blank=True, null=True)

    calle = models.CharField(max_length=200 ,default=None, blank=True, null=True)
    numero = models.CharField(max_length=10, default=None, blank=True, null=True)
    ciudad = models.CharField(max_length=200, default=None, blank=True, null=True)
    cod_postal = models.CharField(max_length=10, default=None, blank=True, null=True)
    pais = models.CharField(max_length=200, default=None, blank=True, null=True)


    fecha_de_nacimiento = models.DateField('fecha de nacimiento')

    tipo = models.OneToOneField(
            CamposCustomOrganizacion,
            related_name='tipo_del_contacto',
            on_delete=models.CASCADE,
            blank=True,
            null=True
        )

    email = models.EmailField(default=None, blank=False, null=False)

    email_alternativo = models.EmailField(default=None, blank=True, null=True)

    sexo = models.OneToOneField(
            CamposCustomOrganizacion,
            related_name='genero_del_contacto',
            on_delete=models.CASCADE,
            blank=True,
            null=True
        )

    origen = models.OneToOneField(
            CamposCustomOrganizacion,
            related_name='origen_del_contacto',
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )

    telefono = models.CharField(max_length=50, default=None, blank=True, null=True)

    movil = models.CharField(max_length=50, default=None, blank=True, null=True)

    recibir_novedades = models.BooleanField(default=False, blank=False)

    observaciones = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.apellido


class Donante(models.Model):
    contacto = models.OneToOneField(Contacto, on_delete=models.CASCADE, blank=True, null=True)

    ESTADOS_DONANTE = [
        (0, 'Activo'),
        (1, 'De Baja'),
        (2, 'En Pausa'),
        (3, 'Completo'),
    ]

    estado = models.IntegerField(choices=ESTADOS_DONANTE, default=0, blank=False, null=False)
    
    FORMAS_PAGO = [
        (0, 'Efectivo'),
        (1, 'Tarjeta de Débito'),
        (2, 'Tarjeta de Crédito'),
        (3, 'Mercado Pago'),
        (4, 'PayPal'),
        (5, 'Otro')
    ]

    forma_de_pago = models.IntegerField(choices=FORMAS_PAGO, default=0, blank=False, null=False)
    
    #Frecuecia figura en el excel como algo obligatorio pero en la documentacion de Slack NO
    FRECUENCIAS_DONANTE = [
        (0, 'Mensual'),
        (1, 'Cada 2 Meses'),
        (2, 'Cada 3 Meses'),
        (3, 'Cada 6 Meses'),
        (4, 'Anual'),
        (5, 'Única Vez'),
    ]

    frecuencia = models.IntegerField(choices=FRECUENCIAS_DONANTE, default=0)

    monto = MoneyField(max_digits=14, decimal_places=2, default_currency='ARS')

    fecha_de_compromiso = models.DateField('fecha de compromiso')

    fecha_de_baja = models.DateField('fecha de baja')

    MOTIVOS_BAJA = [
        (0, 'No puede seguir pagando'),
        (1, 'Disconformidad'),
        (2, 'No quiere informar'),
        (3, 'Otro'),
    ]

    motivo_de_baja = models.IntegerField(choices=MOTIVOS_BAJA, default=0)

class Voluntario(models.Model):
    contacto = models.OneToOneField(Contacto, on_delete=models.CASCADE, blank=True, null=True)
    
    TURNOS_VOLUNTARIOS = [
        (0, 'Mañana'),
        (1, 'Tarde'),
    ]

    turno = models.IntegerField(choices=TURNOS_VOLUNTARIOS, default=0, blank=True, null=True)

    DIAS_PARTICIPACION = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miercoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sabado'),
        (6, 'Domingo'),
    ]

    dias_que_participa = models.IntegerField(choices=DIAS_PARTICIPACION, default=0, blank=True, null=True)

    LISTA_HABILIDADES = [
        (0, 'Informatica'),
        (1, 'Electricidad'),
        (2, 'Carpinteria'),
        (3, 'Otras'),
    ]

    habilidades = models.IntegerField(choices=LISTA_HABILIDADES, default=0, blank=True, null=True)    












