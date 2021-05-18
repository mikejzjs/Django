from django.shortcuts import redirect, render
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
    
    if request.method == 'GET':
        form = TareaForm()
        contexto = {
            'form':form
        }
    else:
        form = TareaForm(request.POST)
        contexto = {'form':form}

    #Si el formulario es válido
    #se usa save() para guardar en la BD
        if form.is_valid():
            form.save()
            return redirect('index')
        print(form)

    return render(request,'Alta.html',contexto)



def editarTarea (request,id):
    tarea = Tarea.objects.get(id = id)
    if request.method == 'GET':
        form = TareaForm(instance = tarea)
        contexto = {'form':form}
    else:
        form = TareaForm(request.POST, instance=tarea)
        contexto = {'form':form}

    if form.is_valid():
       form.save()
       return redirect('index')


    return render (request, 'Alta.html',contexto)



def eliminarTarea(reques, id):
    tarea = Tarea.objects.get(id = id)
    tarea.delete()
    return redirect('index')