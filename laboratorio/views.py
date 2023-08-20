from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all().order_by('id')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'laboratorios':laboratorios,
        'num_visits': num_visits,
    }
    return render(request,'read.html', context)


def insertar_lab(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre,
                                  ciudad=ciudad, 
                                  pais=pais)
        laboratorio.save()
        return redirect('/laboratorio/mostrar')
    else:
        return render(request, 'create.html')

        
def editar_lab(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    context = {
        'laboratorio': laboratorio,
    }
    return render(request=request, template_name='update.html', context=context)
    
    
def actualizarlaboratorio(request, id):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.nombre = nombre
    laboratorio.ciudad = ciudad
    laboratorio.pais = pais
    laboratorio.save()
    return redirect('/laboratorio/mostrar')


def eliminar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/laboratorio/mostrar')
    context = {
        'laboratorio': laboratorio,
    }
    return render(request, 'delete.html', context)
