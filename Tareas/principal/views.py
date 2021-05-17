from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm

# Create your views here.


def saludo(request):

#objects campo, manejador, administrador de comunicar el modelo con sql
#ORM
    #enviar datos al template con contexto=diccionario
    tareas = Tarea.objects.all()
    #Información que será enviada al Template
    contexto = {
        'tareas':tareas
    }
    print(tareas)
    return render(request,'index.html',contexto)


def altaTarea(request):

     return render(request,'Alta.html')
 
 
    