from django.urls import path,include
from rest_framework.routers import DefaultRouter
from TipoCitas.views import *

router=DefaultRouter()
router.register('tipocita',TipoCitasAPI)

urlpatterns = [
    path('crud/',include(router.urls))
]