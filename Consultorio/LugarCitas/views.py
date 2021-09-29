from LugarCitas.serializers import *
from rest_framework import viewsets
from LugarCitas.models import *

class LugarCitasAPI(viewsets.ModelViewSet):
    serializer_class=LugarCitasSerial
    queryset=LugarCita.objects.all()

class TipoProcedimientoAPI(viewsets.ModelViewSet):
    serializer_class=TipoProcedimientoSerial
    queryset=TipoProcedimiento.objects.all()