from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from django.contrib import messages

# Create your views here.

def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

def estadoInsumo(request):
    return render (request, 'Insumos/Insumos.html', )


def edicionInsumos(request, idInsumo):
   insumo = Insumo.objects.get(idInsumo = idInsumo)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

def editarInsumo (request, idInsumo):
    idInsumo = request.POST['id']
    nombreI = request.POST['txtNombre']
    cantidad = request.POST['cantidad']
    tipoUnidad = request.POST['tipoUnidad']
    estado = request.POST['Estado']
    errorIr= []
    actualizar = Insumo.objects.get(idInsumo = idInsumo)
    actualizar.nombreInsumo = nombreI
    nombreP= Insumo.objects.filter(idInsumo= idInsumo).values('nombreInsumo')[0]['nombreInsumo']
    if Insumo.objects.filter(nombreInsumo= nombreP):
        actualizar.cantidad = cantidad
        actualizar.tipoUnidad =  tipoUnidad
        actualizar.estado = estado
        errorIr.clear()
        actualizar.save()
        return redirect('Insumos')
    else:
        if Insumo.objects.filter(nombreInsumo = actualizar.nombreInsumo).exists():
            errorIr.append(1)
            context={"errorIr":errorIr}
            return render(request, 'Inusmos/Editar-Insumo.html',context)
        else:
            actualizar.cantidad = cantidad
            actualizar.tipoUnidad =  tipoUnidad
            actualizar.estado = estado
            errorIr.clear()
            actualizar.save()
            return redirect('Insumos')
        
def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')