from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages

# Create your views here.

def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})


def edicionInsumos(request, idInsumo):
   insumo = Insumo.objects.get(idInsumo = idInsumo)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

def editarInsumo (request):
    idInsumo = request.POST['id']
    nombreInsumo = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.nombreInsumo = nombreInsumo
    insumo.cantidad = cantidad
    insumo.save()
    return redirect('Insumos')

def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')