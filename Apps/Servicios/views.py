from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Servicios.models import Servicios, Servicios_Insumo
from Apps.Citas.models import *
from Apps.Insumos.models import Insumo
from Apps.Servicios.forms import *
import json
from multiprocessing import context
from Apps.Servicios.forms import *
from django.contrib.auth.decorators import permission_required

@permission_required('Servicios.view_servicios',raise_exception=True) 
def servicio(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"Servicios/Servicios.html",context)

@permission_required('Servicios.view_servicios',raise_exception=True) 
def formularioServicio(request,id):
    insumo=Insumo.objects.filter()
    mostrar=Servicios.objects.filter(idServicio=id).first()
    context={"insumo":insumo,'idServicio':id, "mostrar":mostrar}
    return render(request,'Servicios/Crear-Servicio.html',context)

@permission_required('Servicios.view_servicios',raise_exception=True) 
def rutaV(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"Servicios/VerificarNombre.html",context)
    
@permission_required('Servicios.view_servicios',raise_exception=True) 
def verificacionServicio(request):
    nombreServicio= request.POST['nServicio']
    tiempoServicio= request.POST['tiempo']
    existe=Servicios.objects.filter(nServicio=nombreServicio).exists()
    idServicio = Servicios.objects.filter(nServicio=nombreServicio).values_list('idServicio', flat=True).first()

    if Servicios.objects.filter(idServicio=idServicio).exists():
            error="El servicio ingresado ya existe. Por favor, ingresa uno diferente."
            contexto={"error":error}
            return render(request,'Servicios/VerificarNombre.html',contexto)
    else:   
        servicios = Servicios(
            nServicio=nombreServicio, 
            tiempo= tiempoServicio,
        )

        servicios.save()
        idServicio= servicios.idServicio
        return redirect('formularioServicio',idServicio)

@permission_required('Servicios.view_servicios',raise_exception=True) 
def editarS(request, id):
    mostrar=Servicios.objects.filter(idServicio=id).first()
    context={"mostrar":mostrar}
    return render(request,"Servicios/VerificarNombreEditar.html",context)

@permission_required('Servicios.view_servicios',raise_exception=True) 
def verificacionServicioEditar(request,id):

    nombreServicio= request.GET['nombre']
    
    idServicio = Servicios.objects.filter(idServicio=id)

    tiempoServicio = request.GET['tiempo']
    estado = request.GET['estado']
    actualizar=Servicios.objects.get(idServicio=id)
    nombrePropio = Servicios.objects.filter(idServicio=id).values('nServicio')[0]['nServicio']
    actualizar.nServicio=nombreServicio
    
    citas = Citas.objects.filter()
    idCitas= Citas.objects.filter(idServicio = id).values_list('idCita', flat=True) #Obtengo las citas asociadas a este servicio
   
    existe = Servicios.objects.filter(nServicio=nombreServicio).exists()
    existePropio = Servicios.objects.filter(nServicio=nombrePropio)
 
    if existe:  
        if actualizar.nServicio==nombrePropio: #Confirmar que el nombre ingresado es el nombre propio
            if estado == "False":
                for citas.idCita in idCitas:
                    idCita = citas.idCita
                    estadoCita = Citas.objects.filter(idCita=idCita).values_list('estado', flat= True).first()

                    if estadoCita != "Finalizado":
                        error="El servicio está aplicándose en una cita en proceso y no puede desactivarse."
                        mostrar=Servicios.objects.filter(idServicio=id).first()
                        context={"error":error,"mostrar":mostrar}
                        return render(request, 'Servicios/VerificarNombreEditar.html',context)
                actualizar.tiempo=tiempoServicio 
                actualizar.estado=estado
                actualizar.save()
                idServicio= actualizar.idServicio
                return redirect('formularioServicio',idServicio)
            else:
                actualizar.tiempo=tiempoServicio 
                actualizar.estado=estado
                actualizar.save()
                idServicio= actualizar.idServicio
                return redirect('formularioServicio',idServicio)

           

        else:
            error="El servicio ingresado ya existe. Por favor, ingresa uno diferente."
            mostrar=Servicios.objects.filter(idServicio=id).first()
            context={"error":error, "mostrar":mostrar}
            return render(request, 'Servicios/VerificarNombreEditar.html',context) #editar  
    else:  
        if estado == "False":
            for citas.idCita in idCitas:
                idCita = citas.idCita
                estadoCita = Citas.objects.filter(idCita=idCita).values_list('estado', flat= True).first()

                if estadoCita != "Finalizado":
                    error="El servicio está aplicándose en una cita en proceso y no puede desactivarse."
                    mostrar=Servicios.objects.filter(idServicio=id).first()
                    return render(request, 'Servicios/VerificarNombreEditar.html',context)
            actualizar.tiempo=tiempoServicio 
            actualizar.estado=estado
            actualizar.save()
            idServicio= actualizar.idServicio
            return redirect('formularioServicio',idServicio)
    actualizar.tiempo=tiempoServicio 
    actualizar.estado=estado
    actualizar.save()
    idServicio= actualizar.idServicio
    return redirect('formularioServicio',idServicio)

    
@permission_required('Servicios.view_servicios',raise_exception=True) 
def editarEstado(request, id):
    servicioActual= Servicios.objects.get(idServicio=id)

    if servicioActual.estado == 1:
        servicioActual.estado=0
        servicioActual.save()
    else:
        servicioActual.estado=1
        servicioActual.save()
    return redirect("Servicio")


@permission_required('Servicios.view_servicios',raise_exception=True) 
def crearServicio(request):
    #PASO 2:
    #Añadir costo del servicio
    data= json.loads(request.body)
    items = data["items"]
    
    servicios=""
    idServicio= request.POST.get('idActual')
    for item in items:

        servicios = Servicios(
            idServicio=item['idActual'],
            nServicio=item['nombre'],
            tiempo=item['tiempo'], 
            valor=item['valor'],
        )

    servicios.save()

    idServicio=servicios.idServicio
   

    for item in items:
        insumoCompra=item['insumo'] 
        idInsumo = Insumo.objects.filter(nombreInsumo=insumoCompra).values('idInsumo')[0]['idInsumo']

        ServiciosxInsumo= Servicios_Insumo(
            idServicio_id=idServicio,
            idInsumo_id=idInsumo,
            cantidadUsada=item['cantidad'],

        )
        ServiciosxInsumo.save()

    return redirect("Servicio")


    
@permission_required('Servicios.view_servicios',raise_exception=True) 
def actualizarS(request, id):
    nombreServicio= request.GET['nombre']
    errorS= []
    tiempoServicio = request.GET['tiempo']
    actualizar=Servicios.objects.get(idServicio=id)
    actualizar.nServicio=nombreServicio 
    
    nombrePropio = Servicios.objects.filter(idServicio=id).values('nServicio')[0]['nServicio']
    if Servicios.objects.filter(nServicio=nombrePropio):
        actualizar.tiempo=tiempoServicio 
        errorS.clear()
        actualizar.save()
        return redirect("Servicio")
    else:   
        if Servicios.objects.filter(nServicio=actualizar.nServicio).exists():
            errorS.append(1)
            context={"errorS":errorS}
            return render(request, 'Servicios/Editar-Servicio.html',context)
        else:
            actualizar.tiempo=tiempoServicio 
            errorS.clear()
            actualizar.save()
            return redirect("Servicio")
     
        
    

@permission_required('Servicios.view_servicios',raise_exception=True) 
def eliminarS(request, id):   
    registro= Servicios.objects.get(idServicio=id)
    registro.delete() 
    return redirect("Servicio")   