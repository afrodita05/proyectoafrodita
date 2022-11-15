from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages

# Create your views here.

def insumos (request):
    insumos = Insumo.objects.all()
    estadoT = ("Activo")
    estadoF = ("Inactivo")
    if insumos == True:
        estado = estadoT
    else:
        estado = estadoF
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

def estadoInsumo(request):
    
    return render (request, 'Insumos/Insumos.html', )


def edicionInsumos(request, idInsumo):
   insumo = Insumo.objects.get(idInsumo = idInsumo)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

def editarInsumo (request):
    idInsumo = request.POST['id']
    nombreInsumo = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']
    estado = request.POST['Estado']
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.nombreInsumo = nombreInsumo
    insumo.cantidad = cantidad
    insumo.estado = estado
    insumo.save()
    return redirect('Insumos')

def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')