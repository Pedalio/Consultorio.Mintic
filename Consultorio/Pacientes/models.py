from django.db import models
from TipoCategoria.models import *

# Create your models here.
class Pacientes(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    identificacion=models.IntegerField(default=0)
    #telefono=models.ForeignKey(telefono, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50) #Crear class
    direccion = models.CharField(max_length=50)
    correo=models.EmailField()
    edad=models.IntegerField(default=1) #Enviar alertas segun la edad
    tipoUsuario=models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombres + " " + self.apellidos + " | " + str(self.tipoUsuario.tipoCategoria)
