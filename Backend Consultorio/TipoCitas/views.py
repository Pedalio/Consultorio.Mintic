from TipoCitas.serializers import TipoCitasSerial
from rest_framework import viewsets
from TipoCitas.models import *

class TipoCitasAPI(viewsets.ModelViewSet):
    serializer_class=TipoCitasSerial
    queryset=tipoCita.objects.all()