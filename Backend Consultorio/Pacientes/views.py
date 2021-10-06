from rest_framework import viewsets
from Pacientes.serializers import *

class PacientesAPI(viewsets.ModelViewSet):
    serializer_class=PacientesSerial
    queryset=Pacientes.objects.all()