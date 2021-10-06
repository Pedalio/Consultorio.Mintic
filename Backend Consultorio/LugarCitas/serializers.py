from rest_framework import serializers
from LugarCitas.models import *

class LugarCitasSerial(serializers.ModelSerializer):
    class Meta:
        model=LugarCita
        fields=['nombre','ciudad','direccion','telefono']

class TipoProcedimientoSerial(serializers.ModelSerializer):
    class Meta:
        model=TipoProcedimiento
        fields=['nombre','especialidad']