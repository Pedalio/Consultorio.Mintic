from rest_framework import serializers
from TipoCitas.models import *

class TipoCitasSerial(serializers.ModelSerializer):
    class Meta:
        model=tipoCita
        fields=['tipo']