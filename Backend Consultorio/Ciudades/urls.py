from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Ciudades.views import *

router = DefaultRouter()
router.register('ciudades',CiudadesAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]