from django.urls import path,include
from rest_framework.routers import DefaultRouter
from TipoCategoria.views import *

router=DefaultRouter()
router.register('tipocategoria',TipoCategoriaAPI)

urlpatterns = [
    path('crud/',include(router.urls))
]