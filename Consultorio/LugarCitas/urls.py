from django.urls import path,include
from rest_framework.routers import DefaultRouter
from LugarCitas.views import *

router = DefaultRouter()
router.register('lugarcita',LugarCitasAPI)
router.register('tipoprocedimiento',TipoProcedimientoAPI)

urlpatterns = [
    path('crud/',include(router.urls))
]