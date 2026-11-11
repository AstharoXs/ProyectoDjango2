from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

# Create your views here.
def home(request):
    tareas=Tarea.objects.all().order_by("id")
    context={'tareas':tareas}
    return render(request, 'todo/home.html',context)

def agregar(request):
    form = TareaForm(request.POST or None)
    if request.method =="POST" and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'todo/agregar.html', {'form': form})

def eliminar(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.delete()
    return redirect("home")