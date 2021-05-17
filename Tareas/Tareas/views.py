from django.http import HttpResponse
from django.template import Template, Context

#Funcion que representa una vista
def saludo(request):

    doc_externo=open("C:/Users/Mike/Desktop/DJango/Django/Tareas/Tareas/Plantillas/Crear_tareas.html")

    plantilla = Template(doc_externo.read())

    doc_externo.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def despedida(request):
    
    return HttpResponse("Adiós vista")


def bienvenida(request):

    return HttpResponse("Hola Vaquero")

def vistaPrueba(request):

    return HttpResponse("Probando Github")