from django.shortcuts import render, redirect
from .models import Insumo
from .forms import Insumo
from Apps.Citas.models import *
from Apps.Servicios.models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('Insumos.view_insumo',raise_exception=True)
def insumos (request):
    insumos = Insumo.objects.all()
    return render (request, 'Insumos/Insumos.html', {'insumos': insumos})

@permission_required('Insumos.view_insumo',raise_exception=True)
def estadoInsumo(request):
    return render (request, 'Insumos/Insumos.html', )

@permission_required('Insumos.view_insumo',raise_exception=True)
def edicionInsumos(request, id):
   insumo = Insumo.objects.get(idInsumo = id)
   return render(request,'Insumos/Editar-Insumo.html', {'insumo':insumo})

@permission_required('Insumos.view_insumo',raise_exception=True)
def editarInsumo (request,id ):
    nombreI = request.POST['txtNombre']
    idInsumo = Insumo.objects.filter(idInsumo =id)
    cantidad = request.POST['cantidad']
    tipoUnidad = request.POST['tipoUnidad']
    estado = request.POST['Estado']
    
    actualizar = Insumo.objects.get(idInsumo = id)
    nombreP= Insumo.objects.filter(idInsumo = id).values('nombreInsumo')[0]['nombreInsumo']
    actualizar.nombreInsumo = nombreI
    servicios = Servicios.objects.filter()
    idServicios= Servicios_Insumo.objects.filter(idInsumo= id).values_list('idServicio', flat=True) #obtengo servicios asociados a este insumo #Obtengo las citas asociadas a este insumo
    existe = Insumo.objects.filter(nombreInsumo=nombreP).exists()
    existePropio = Insumo.objects.filter(nombreInsumo=nombreP)
    
    if existe:  
        if actualizar.nombreInsumo==nombreP: #Confirmar que el nombre ingresado es el nombre propio
            if estado == "False":
                for servicios.idServicio in idServicios:
                    idServicio = servicios.idServicio
                    estadoCita = Citas.objects.filter(idServicio=idServicio).values_list('estado', flat= True).first()

                    if estadoCita != "Finalizado":
                        error="El Insumo está aplicándose en una cita en proceso y no puede desactivarse."
                        mostrar=Insumo.objects.filter(idInsumo = id).first()
                        return render(request, 'Insumos/Editar-Insumo.html',context)
                actualizar.cantidad=cantidad
                actualizar.estado=estado
                actualizar.tipoUnidad=tipoUnidad
                actualizar.save()
                idInsumo= actualizar.idInsumo
                return redirect('Insumos')
            else:
                actualizar.cantidad=cantidad
                actualizar.estado=estado
                actualizar.tipoUnidad=tipoUnidad
                actualizar.save()
                idInsumo= actualizar.idInsumo
                return redirect('Insumos')
        else:
            error="El Insumo ingresado ya existe. Por favor, ingresa uno diferente."
            mostrar=Insumo.objects.filter(idInsumo = id).first()
            context={"error":error, "mostrar":mostrar}
            return render(request, 'Insumos/Editar-Insumo.html',context) #editar  
    else:
        if estado == "False":
            for servicios.idServicio in idServicios:
                idServicio = servicios.idServicio
                estadoCita = Citas.objects.filter(idServicio=idServicio).values_list('estado', flat= True).first()

                if estadoCita != "Finalizado":
                    error="El Insumo está aplicándose en una cita en proceso y no puede desactivarse."
                    mostrar=Insumo.objects.filter(idInsumo = id).first()
                    return render(request, 'Insumos/Editar-Insumo.html',context)
            actualizar.cantidad=cantidad
            actualizar.estado=estado
            actualizar.tipoUnidad=tipoUnidad
            actualizar.save()
            idInsumo= actualizar.idInsumo
            return redirect('Insumos')
    actualizar.cantidad=cantidad
    actualizar.estado=estado
    actualizar.tipoUnidad=tipoUnidad
    actualizar.save()
    idInsumo= actualizar.idInsumo
    return redirect('Insumos')


@permission_required('Insumos.view_insumo',raise_exception=True)
def eliminarInsumos(request, idInsumo):
    insumo = Insumo.objects.get(idInsumo = idInsumo)
    insumo.delete()
    messages.success(request, "Insumo eliminado exitosamente")
    return redirect('Insumos')