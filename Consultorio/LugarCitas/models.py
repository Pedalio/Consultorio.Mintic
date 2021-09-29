from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from Ciudades.models import ciudades
from Medicos.models import *

# Create your models here.
class LugarCita(models.Model):
    nombre=models.CharField(max_length=100)
    ciudad=models.ForeignKey(ciudades, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=100)
    #geolocalizacion=> Pendiente
    telefono=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre + " - " + self.ciudad.nombre

class TipoProcedimiento(models.Model):
    #identID=models.CharField() =>pendiente
    nombre=models.CharField(max_length=300)
    especialidad=models.ForeignKey(Especialidades, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.especialidad.nombre + " : " + self.nombre