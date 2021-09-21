from django.urls import path
from django.urls.resolvers import URLPattern
from Servicios.views import vistaServicios
#Servicios - Aplicacion
#No es obligatorio pero si recomendable

urlpatterns = [
    path('servicios', vistaServicios)
]
