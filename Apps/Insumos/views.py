from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages

# Create your views here.

def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

<<<<<<< HEAD
def crearInsumos (request):
    nombreInsumo = request.POST['Nombre']
    unidades = request.POST['Unidad']
    gramos = request.POST['Gramos']
    insumo = Insumo.objects.create(nombreInsumo = nombreInsumo, unidades= unidades, gramos = gramos)
    messages.success(request, "Creado exitosamente")
    return redirect('Insumos')
=======
>>>>>>> 7b4a5018eefa1eb68f4c2fc8e09ab0ed29669771

def edicionInsumos(request, idInsumo):
   insumo = Insumo.objects.get(idInsumo = idInsumo)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

def editarInsumo (request):
    idInsumo = request.POST['id']
<<<<<<< HEAD
    nombreInsumo = request.POST['Nombre']
    unidad = request.POST['Unidad']
    gramos = request.POST['Gramos']
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.nombreInsumo = nombreInsumo
    insumo.unidad = unidad
    insumo.gramos = gramos
=======
    nombreInsumo = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.nombreInsumo = nombreInsumo
    insumo.cantidad = cantidad
>>>>>>> 7b4a5018eefa1eb68f4c2fc8e09ab0ed29669771
    insumo.save()
    return redirect('Insumos')

def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')