from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from djmoney.models.fields import MoneyField

class Organizacion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha_alta = models.DateTimeField('fecha de alta')
    
    class Meta:
        verbose_name_plural = 'organizaciones'

    def __str__(self):
        return self.nombre

            

class Cuenta(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

#########################################
###########     CONTACTO    #############
#########################################

class Contacto(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    apellido = models.CharField(max_length=200, default=None, blank=False, null=False)

    TIPOS_CONTACTO = [
        (0, 'General'),
        (1, 'Donante'),
        (2, 'Voluntario'),
        (3, 'Ambos'),
        
    ]

    tipo = models.IntegerField(choices=TIPOS_CONTACTO, default=0, verbose_name='Tipo de Contacto')


    email = models.EmailField(default=None, blank=True, null=True)

    SEXOS_CONTACTO = [
        (0, 'Hombre'),
        (1, 'Mujer'),
        (2, 'No Aplica')
    ]

    sexo = models.IntegerField(choices=SEXOS_CONTACTO, default=None, blank=True, null=True)

    telefono = models.CharField(max_length=50, default=None, blank=True, null=True)

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

    estado = models.IntegerField(choices=ESTADOS_DONANTE, default=0)

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

    fecha_de_compromiso = models.DateTimeField('fecha de compromiso')

class Voluntario(models.Model):
    contacto = models.OneToOneField(Contacto, on_delete=models.CASCADE, blank=True, null=True)
    
    TURNOS_VOLUNTARIOS = [
        (0, 'Mañana'),
        (1, 'Tarde'),
    ]

    turno = models.IntegerField(choices=TURNOS_VOLUNTARIOS, default=0, blank=True, null=True)
        
        
