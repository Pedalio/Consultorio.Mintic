from LugarCitas.models import LugarCita, TipoProcedimiento
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

from Medicos.models import *
from Pacientes.models import *
from TipoCitas.models import *


#Tener en cuenta los descuentos de los medicos

# Create your models here.




class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    tipocita=models.ForeignKey(tipoCita, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medicos, on_delete=models.CASCADE)
    horaCita=models.ForeignKey(HorasCitasDiarias,on_delete=models.CASCADE)
    tipoServicio = models.ForeignKey(TipoProcedimiento, on_delete=models.CASCADE)
    lugar = models.ForeignKey(LugarCita, on_delete=models.CASCADE)
    recomendaciones="Recuerde llegar mínimo 15 minutos antes de la cita"

    def __str__(self) -> str:
        return self.paciente.nombres + " | " +  str(self.horaCita.diaSemana) +  " | "  +  str(self.horaCita.horaDia) + " | " + self.recomendaciones
    
    def cambio_Fecha(self):
        pass

    def cambio_Lugar(self):
        pass

    def eliminar_Cita(self):
        pass

