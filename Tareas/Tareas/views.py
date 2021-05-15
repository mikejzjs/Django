from django.http import HttpResponse

#Funcion que representa una vista
def saludo(request):

    return HttpResponse("Hola Mundo")


def despedida(request):
    
    return HttpResponse("Adiós vista")


def bienvenida(request):

    return HttpResponse("Hola Vaquero")

def vistaPrueba(request):

    return HttpResponse("Probando Github")