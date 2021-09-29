from django.db import models

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
    correo = models.EmailField(blank=True, null=True)
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

