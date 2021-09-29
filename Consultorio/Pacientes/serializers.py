from rest_framework import serializers
from Pacientes.models import *

class PacientesSerial(serializers.ModelSerializer):
    class Meta:
        model=Pacientes
        fields=['nombres','apellidos','identificacion','telefono','direccion','correo','edad','tipoUsuario']