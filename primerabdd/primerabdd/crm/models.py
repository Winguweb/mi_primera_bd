from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Organizacion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=200)
    #username = models.CharField(max_length=20)
    #password = models.CharField(max_length=30, default='')
    fecha_alta = models.DateTimeField('fecha de alta')
    
    class Meta:
        verbose_name_plural = 'organizaciones'

    def __str__(self):
        return self.nombre

            

class Cuenta(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    cantidad_contactos = lambda self : self.contacto_set.count()

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        
        
