from rest_framework import viewsets
from Citas.serializers import *

class CitasAPI(viewsets.ModelViewSet):
    serializer_class=CitasSerial
    queryset=Citas.objects.all()