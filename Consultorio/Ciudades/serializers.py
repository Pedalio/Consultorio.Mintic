from rest_framework import serializers
from Ciudades.models import *

class CiudadesSerial(serializers.ModelSerializer):
    class Meta:
        model=ciudades
        fields=['nombre']