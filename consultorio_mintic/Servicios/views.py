from django.http.response import HttpResponse
from django.shortcuts import render
#Para imprimir mensajes sencillos de respuesta
from django.http import HttpResponse

# Create your views here.

def vistaServicios(request):
    """
    request -> contiene toda la infrmacion
    del usuario que hace la peticion de acceso a
    la aplicacion a traves de metodos GET y POST
    principalment
    
    GET     -> método con el cual el usuario
               solicita acceder a una URL.
    
    POST    -> método con el cual el usuario 
               envía información a una URL.
e


    """

    return HttpResponse("Hola estas entrando a la vista de Servicios")