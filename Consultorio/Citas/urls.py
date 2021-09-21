from django.urls import path
from django.urls.resolvers import URLPattern

from Citas.views import vistaEjemplo

urlpatterns = [
    path('citas', vistaEjemplo)
]