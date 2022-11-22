from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
# Create your views here.

@permission_required('Insumos.view_insumo') 
def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

@permission_required('Insumos.view_insumo') 

def edicionInsumos(request, idInsumo):
   insumo = Insumo.objects.get(idInsumo = idInsumo)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

@permission_required('Insumos.view_insumo') 

def editarInsumo (request):
    idInsumo = request.POST['id']
    nombreInsumo = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.nombreInsumo = nombreInsumo
    insumo.cantidad = cantidad
    insumo.save()
    return redirect('Insumos')

@permission_required('Insumos.view_insumo') 

def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')