from rest_framework import serializers
from TipoCategoria.models import *

class TipoCategoriaSerial(serializers.ModelSerializer):
    class Meta:
        model=TipoCategoria
        fields = ['tipoCategoria','valorCategoria']