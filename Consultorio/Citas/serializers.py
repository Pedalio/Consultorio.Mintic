from rest_framework import serializers
from Citas.models import *

class CitasSerial(serializers.ModelSerializer):
    class Meta:
        model=Citas
        fields = ['paciente','tipoCita','medico','horaCita','tipoServicio','lugar','recomendaciones']
        