from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from Citas.models import *

#Tener en cuenta los descuentos de los medicos

# Create your models here.

class DiaSemana(models.Model):
    diaSemana=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.diaSemana



class Especialidades(models.Model):
    nombre=models.CharField(max_length=200)
    #tarifa=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nombre #+ " : " + str(self.tarifa)


class TipoProcedimiento(models.Model):
    #identID=models.CharField() =>pendiente
    nombre=models.CharField(max_length=300)
    especialidad=models.ForeignKey(Especialidades, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.especialidad.nombre + " : " + self.nombre


class tipoCita(models.Model):
    tipo=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tipo


class Ciudades(models.Model):
    nombre=models.CharField(max_length=50)
    #codigo=models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre


class LugarCitas(models.Model):#Centro Medico
    nombre=models.CharField(max_length=100)
    ciudad=models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=100)
    #geolocalizacion=> Pendiente
    telefono=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre + " - " + self.ciudad.nombre


class TipoCategoria(models.Model):
    tipoCategoria=models.CharField(max_length=20)
    valorCategoria=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.tipoCategoria + " - " + str(self.valorCategoria)


'''class telefono(models.Model):
    numTelefono=models.IntegerField(default=0)
    numWhatsapp=models.IntegerField(default=0)
    numTelefonoFijo=models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.numWhatsapp)
'''

class Pacientes(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    identificacion=models.IntegerField(default=0)
    #telefono=models.ForeignKey(telefono, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50) #Crear class
    direccion = models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField(default=1) #Enviar alertas segun la edad
    tipoUsuario=models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombres + " " + self.apellidos + " | " + str(self.tipoUsuario.tipoCategoria)


class Medicos(models.Model):
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    descripcionPersonal = models.TextField(max_length=500, blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    identificacion = models.IntegerField(default=0)
    numTarjetaProfesional = models.CharField(max_length=20)
    #telefono = models.ForeignKey(telefono, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    edad = models.IntegerField(default=1, blank=True, null=True)
    horariosDisponibles = models.DateTimeField(auto_now_add=True)
    #horariosDisponibles=models.ForeignKey(HorasCitasDiarias, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombres + " " + self.apellidos + "| "+  self.especialidad.nombre + "| Tarjeta Profesional: " + self.numTarjetaProfesional


class HorasCitasDiarias(models.Model):
    horaDia = models.TimeField()
    diaSemana=models.ForeignKey(DiaSemana, on_delete=models.CASCADE)
    nombreMedico=models.ForeignKey(Medicos,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.diaSemana.diaSemana + " - " + str(self.horaDia) + " | " + self.nombreMedico.nombres


class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    tipocita=models.ForeignKey(tipoCita, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medicos, on_delete=models.CASCADE)
    horaCita=models.ForeignKey(HorasCitasDiarias,on_delete=models.CASCADE)
    #fechaServicio = models.DateField()
    #horaServicio = models.TimeField()#Sale
    tipoServicio = models.ForeignKey(TipoProcedimiento, on_delete=models.CASCADE)
    lugar = models.ForeignKey(LugarCitas, on_delete=models.CASCADE)
    recomendaciones="Recuerde llegar mínimo 15 minutos antes de la cita"

    def __str__(self) -> str:
        return self.paciente.nombres + " | " +  str(self.horaCita.diaSemana) +  " | "  +  str(self.horaCita.horaDia) + " | " + self.recomendaciones
    
    def cambio_Fecha(self):
        pass

    def cambio_Lugar(self):
        pass

    def eliminar_Cita(self):
        pass

