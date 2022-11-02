from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Servicios.models import Servicios, Servicios_Insumo
from Apps.Insumos.models import Insumo
import json
from multiprocessing import context

def servicio(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"Servicios/Servicios.html",context)


def formularioServicio(request):
    insumo=Insumo.objects.filter()
    context={"insumo":insumo}   
    return render(request,'Servicios/Crear-Servicio.html',context)


def crearServicio(request):
    data= json.loads(request.body)
    items = data["items"]
    print(items,type(items))
    servicios=""

    for item in items:

        servicios = Servicios(
            nServicio=item['nombre'],
            tiempo=item['tiempo'], 
        )

    servicios.save()

    idServicio=servicios.idServicio

    for item in items:
        insumoCompra=item['insumo'] 
        idInsumo = Insumo.objects.filter(nombre=insumoCompra).values('idInsumo')[0]['idInsumo']

        ServiciosxInsumo= Servicios_Insumo(
            idServicio_id=idServicio,
            idInsumo_id=idInsumo

        )
        ServiciosxInsumo.save()

    return redirect("Servicio")

    # DCompra=Detalle_Compra(
    #     idCompra_id=idCompra,
    #     idInsumo_id=idInsumo
    #     )
    #     DCompra.save()

    # # Crear tabla intermedia y guardar los valores correspondientes utilizando la view
    
    # errorS= []
    # if Servicios.objects.filter(nServicio=nombreServicio).exists():
      
    #     errorS.append(1)
    #     context={"errorS":errorS}
    #     return render(request, 'Servicios/Crear-Servicio.html',context)
    # else:
    #     tiempoServicio= request.POST['tiempo']
    #     servicios=Servicios(nServicio=nombreServicio,tiempo=tiempoServicio) 
    #     errorS.clear()
    #     servicios.save()
    




def editarS(request, id):
    mostrar=Servicios.objects.filter(idServicio=id).first()
    context={"mostrar":mostrar}
    return render(request,"Servicios/Editar-Servicio.html",context)
    

def actualizarS(request, id):
    nombreServicio= request.GET['nombre']
    errorS= []
    tiempoServicio = request.GET['tiempo']
    actualizar=Servicios.objects.get(idServicio=id)
    actualizar.nServicio=nombreServicio #Será este?
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
     
        
    


def eliminarS(request, id):   
    registro= Servicios.objects.get(idServicio=id)
    registro.delete() 
    return redirect("Servicio")    


# Create your views here.
# class Servicioview(TemplateView):
#     pass

# Servicios= Servicioview.as_view(
#     template_name="Servicios/Servicios.html",
# )
# Crear_Servicio= Servicioview.as_view(
#     template_name="Servicios/Crear-Servicio.html",
# )
# Editar_Servicio= Servicioview.as_view(
#     template_name="Servicios/Editar-Servicio.html",
# )
# Detalle_Servicio= Servicioview.as_view(
#     template_name="Servicios/Ver-Detalle.html",
# )
