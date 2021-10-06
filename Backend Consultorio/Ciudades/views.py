from Ciudades.serializers import CiudadesSerial
from rest_framework import viewsets
from Ciudades.models import *

class CiudadesAPI(viewsets.ModelViewSet):
    serializer_class=CiudadesSerial
    queryset=ciudades.objects.all()