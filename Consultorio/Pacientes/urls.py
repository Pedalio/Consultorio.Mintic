from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Pacientes.views import *

router = DefaultRouter()
router.register('pacientes',PacientesAPI)

urlpatterns = [
    path('crud/',include(router.urls))
]