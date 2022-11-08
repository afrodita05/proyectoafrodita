from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages

# Create your views here.

def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

def crearInsumos (request):
    nombreInsumo = request.POST['Nombre']
    unidades = request.POST['Unidad']
    gramos = request.POST['Gramos']
    insumo = Insumo.objects.create(nombreInsumo = nombreInsumo, unidades= unidades, gramos = gramos)
    messages.success(request, "Creado exitosamente")
    return redirect('Insumos')

def edicionInsumos(request, idInsumo):
   insumo = Insumo.objects.get(idInsumo = idInsumo)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

def editarInsumo (request):
    idInsumo = request.POST['id']
    nombreInsumo = request.POST['Nombre']
    unidad = request.POST['Unidad']
    gramos = request.POST['Gramos']
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.nombreInsumo = nombreInsumo
    insumo.unidad = unidad
    insumo.gramos = gramos
    insumo.save()
    return redirect('Insumos')

def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')