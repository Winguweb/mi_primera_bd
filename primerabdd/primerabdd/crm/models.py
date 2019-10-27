from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from djmoney.models.fields import MoneyField





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
class CampoCustomOrigen(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    origen = models.CharField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return (self.origen)

class CampoCustomTipoContacto(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return (self.tipo)

class CampoCustomTipoCuenta(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return (self.tipo) 

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
            CampoCustomTipoCuenta,
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
    
    TIPOS_CONTACTO = [
        (0, 'General'),
        (1, 'Donante'),
        (2, 'Voluntario'),
        (3, 'Ambos'),
    ]

    tipo = models.IntegerField(choices=TIPOS_CONTACTO, default=0, verbose_name='Tipo de Contacto', blank=True, null=True)
    
    #LO CAMBIO A CATEGORIA DE FORMA PROVISORIA
    categoria = models.OneToOneField(
            CampoCustomTipoContacto,
            on_delete=models.CASCADE,
            blank=True,
            null=True
        )

    email = models.EmailField(default=None, blank=False, null=False)

    email_alternativo = models.EmailField(default=None, blank=True, null=True)

    OPCIONES_GENERO = [
        (0, 'Masculino'),
        (1, 'Femenino'),
        (2, 'Otro'),
    ]
    
    sexo = models.IntegerField(choices=OPCIONES_GENERO, blank=False, null=False, default=2)


    origen = models.OneToOneField(
            CampoCustomOrigen,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )

    telefono = models.CharField(max_length=50, default=None, blank=True, null=True)

    movil = models.CharField(max_length=50, default=None, blank=True, null=True)

    recibir_novedades = models.BooleanField(default=False, blank=False)

    observaciones = models.TextField(default=None, blank=True, null=True)

    es_voluntario = models.BooleanField(default=False, blank=False, null=False)

    TURNOS_VOLUNTARIOS = [
        (0, 'Mañana'),
        (1, 'Tarde'),
    ]

    turno = models.IntegerField(choices=TURNOS_VOLUNTARIOS, blank=True, null=True)

    ESTADO = [
        (0, 'Activo'),
        (1, 'Inactivo'),
    ]

    estado = models.IntegerField(choices=ESTADO, blank=True, null=True)

    LISTA_HABILIDADES = [
        (0, 'Informatica'),
        (1, 'Electricidad'),
        (2, 'Carpinteria'),
        (3, 'Otras'),
    ]

    habilidades = models.IntegerField(choices=LISTA_HABILIDADES, blank=True, null=True) 
    

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

    turno = models.IntegerField(choices=TURNOS_VOLUNTARIOS, blank=True, null=True)

    ESTADO = [
        (0, 'Activo'),
        (1, 'Inactivo'),
    ]

    estado = models.IntegerField(choices=ESTADO, blank=True, null=True)

    LISTA_HABILIDADES = [
        (0, 'Informatica'),
        (1, 'Electricidad'),
        (2, 'Carpinteria'),
        (3, 'Otras'),
    ]

    habilidades = models.IntegerField(choices=LISTA_HABILIDADES, blank=True, null=True)    












