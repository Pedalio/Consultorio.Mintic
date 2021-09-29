from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citas/api/', include('Citas.urls')),
    path('ciudades/api/', include('Ciudades.urls')),
    path('lugarcitas/api/', include('LugarCitas.urls')),
    path('medicos/api/',include('Medicos.urls')),
    path('pacientes/api/',include('Pacientes.urls')),
    path('tipocategoria/api/',include('TipoCategoria.urls')),
    path('tipocitas/api/',include('TipoCitas.urls')),
]