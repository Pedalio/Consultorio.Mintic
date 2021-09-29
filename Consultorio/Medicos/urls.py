from django.urls import path,include
from rest_framework.routers import DefaultRouter

from Medicos.views import *

router = DefaultRouter()
router.register('medicos', MedicosAPI)
router.register('diasemana', DiaSemanaAPI)
router.register('especialidades', EspecialidadesAPI)
router.register('horascitasdiarias', HorasCitasDiariasAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]