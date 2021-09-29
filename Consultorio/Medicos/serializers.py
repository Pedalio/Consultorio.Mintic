from rest_framework import serializers
from Medicos.models import *

class MedicosSerial(serializers.ModelSerializer):
    class Meta:
        model=Medicos
        fields = ['especialidad','descripcionPersonal','imagen','nombres','apellidos','identificacion','numTarjetaProfesional','telefono','direccion','correo','edad','horariosDisponibles']

class DiaSemanaSerial(serializers.ModelSerializer):
    class Meta:
        model=DiaSemana
        fields = ['diaSemana']

class EspecialidadesSerial(serializers.ModelSerializer):
    class Meta:
        model=Especialidades
        fields = ['nombre']
    
class HorasCitasDiariasSerial(serializers.ModelSerializer):
    class Meta:
        model=HorasCitasDiarias
        fields=['horaDia','diaSemana','nombreMedico']