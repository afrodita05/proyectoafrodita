from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Servicios.models import Servicios, Servicios_Insumo
from Apps.Insumos.models import Insumo
from Apps.Servicios.forms import *
import json
from multiprocessing import context
from Apps.Servicios.forms import *
from django.contrib.auth.decorators import permission_required

@permission_required('Servicios.view_servicios') 
def servicio(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"Servicios/Servicios.html",context)

@permission_required('Servicios.view_servicios') 
def formularioServicio(request,id):
    insumo=Insumo.objects.filter()
    mostrar=Servicios.objects.filter(idServicio=id).first()
    context={"insumo":insumo,'idServicio':id, "mostrar":mostrar}
    return render(request,'Servicios/Crear-Servicio.html',context)

@permission_required('Servicios.view_servicios') 
def rutaV(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"Servicios/VerificarNombre.html",context)
    
@permission_required('Servicios.view_servicios') 
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

@permission_required('Servicios.view_servicios') 
def editarS(request, id):
    mostrar=Servicios.objects.filter(idServicio=id).first()
    context={"mostrar":mostrar}
    return render(request,"Servicios/VerificarNombreEditar.html",context)

@permission_required('Servicios.view_servicios') 
def verificacionServicioEditar(request,id):

    nombreServicio= request.GET['nombre']
    
    idServicio = Servicios.objects.filter(idServicio=id)

    tiempoServicio = request.GET['tiempo']
    actualizar=Servicios.objects.get(idServicio=id)
    nombrePropio = Servicios.objects.filter(idServicio=id).values('nServicio')[0]['nServicio']
    actualizar.nServicio=nombreServicio
    

    existe = Servicios.objects.filter(nServicio=nombreServicio).exists()
    existePropio = Servicios.objects.filter(nServicio=nombrePropio)
 
    if existe:  
        
        if actualizar.nServicio==nombrePropio: #Confirmar que el nombre ingresado es el nombre propio
           
            actualizar.tiempo=tiempoServicio 
            actualizar.save()
            idServicio= actualizar.idServicio
            return redirect('formularioServicio',idServicio)

        else:
            error="El servicio ingresado ya existe. Por favor, ingresa uno diferente."
            mostrar=Servicios.objects.filter(idServicio=id).first()
            context={"error":error, "mostrar":mostrar}
            return render(request, 'Servicios/VerificarNombreEditar.html',context) #editar
     
    else:  
        actualizar.tiempo=tiempoServicio 
        actualizar.save()
        idServicio= actualizar.idServicio
        return redirect('formularioServicio',idServicio)
    



@permission_required('Servicios.view_servicios') 
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


    
@permission_required('Servicios.view_servicios') 
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
     
        
    

@permission_required('Servicios.view_servicios') 
def eliminarS(request, id):   
    registro= Servicios.objects.get(idServicio=id)
    registro.delete() 
    return redirect("Servicio")   