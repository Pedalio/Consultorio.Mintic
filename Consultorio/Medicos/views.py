from rest_framework import viewsets
from Medicos.serializers import *

class MedicosAPI(viewsets.ModelViewSet):
    serializer_class=MedicosSerial
    queryset=Medicos.objects.all()

class DiaSemanaAPI(viewsets.ModelViewSet):
    serializer_class=DiaSemanaSerial
    queryset=DiaSemana.objects.all()

class EspecialidadesAPI(viewsets.ModelViewSet):
    serializer_class=EspecialidadesSerial
    queryset=Especialidades.objects.all()

class HorasCitasDiariasAPI(viewsets.ModelViewSet):
    serializer_class=HorasCitasDiariasSerial
    queryset=HorasCitasDiarias.objects.all()