from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Servicios.models import Servicios

def servicio(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"Servicios/Servicios.html",context)


def formularioServicio(request):
    return render(request,'Servicios/Crear-Servicio.html')


def crearServicio(request):
    nombreServicio= request.POST['nombre']
    errorS= []
    if Servicios.objects.filter(nServicio=nombreServicio).exists():
      
        errorS.append(1)
        context={"errorS":errorS}
        return render(request, 'Servicios/Crear-Servicio.html',context)
    else:
        tiempoServicio= request.POST['tiempo']
        servicios=Servicios(nServicio=nombreServicio,tiempo=tiempoServicio) 
        errorS.clear()
        servicios.save()
    return redirect("Servicio")


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
