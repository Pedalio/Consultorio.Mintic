from rest_framework import viewsets
from TipoCategoria.serializers import *

class TipoCategoriaAPI(viewsets.ModelViewSet):
    serializer_class=TipoCategoriaSerial
    queryset=TipoCategoria.objects.all()