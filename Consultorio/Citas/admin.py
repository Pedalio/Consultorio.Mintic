from Ciudades.models import ciudades
from django.contrib import admin
from Citas.models import *
from Ciudades.models import *
from Ciudades.models import *
from LugarCitas.models import *
from Medicos.models import *
from Pacientes.models import *
from TipoCategoria.models import *
from TipoCitas.models import *


# Register your models here.
admin.site.register(TipoCategoria)
admin.site.register(Especialidades)
admin.site.register(LugarCita)
admin.site.register(Pacientes)
admin.site.register(Medicos)
admin.site.register(Citas)
admin.site.register(ciudades)
admin.site.register(DiaSemana)
admin.site.register(HorasCitasDiarias)
admin.site.register(tipoCita)