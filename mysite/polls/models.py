import datetime

from django.db import models
from django.utils import timezone


class Cuenta(models.Model):
    cuenta_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.cuenta_texto

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Contacto(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre