from django.db import models

class Cuenta(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad_contactos = lambda self : self.contacto_set.count()

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        
        
