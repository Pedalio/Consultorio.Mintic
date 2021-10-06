from django.urls import path, include       #Añadir direcciones locales (individual/grupal)
from rest_framework.routers import DefaultRouter    #Gestion de API'S tipo 'ViewSet'

from Citas.views import *

router = DefaultRouter()
router.register('citas', CitasAPI)

urlpatterns=[
    #Lista de direcciones locales
    path('crud/', include(router.urls))
]