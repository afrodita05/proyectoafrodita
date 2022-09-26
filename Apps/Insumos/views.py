from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages

# Create your views here.

def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

def crearInsumos (request):
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']
    insumo = Insumo.objects.create(nombre = nombre, cantidad= cantidad)
    messages.success(request, "Creado exitosamente")
    return redirect('Insumos')

def edicionInsumos(request, idInsumos):
   insumo = Insumo.objects.get(idInsumos = idInsumos)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

def editarInsumo (request):
    idInsumos = request.POST['id']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']
    insumo = Insumo.objects.get(idInsumos = idInsumos)
    insumo.nombre = nombre
    insumo.cantidad = cantidad
    insumo.save()
    return redirect('Insumos')

def eliminarInsumos(request, idInsumos):
    insumo = Insumo.objects.get(idInsumos = idInsumos)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')