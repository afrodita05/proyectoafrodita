from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Configuracion.models import Rol
# Create your views here.

def crearRol(request): 
         
    nombreRol=request.POST['nombre']


    configuracionRol=request.POST['configuracion']
    insumosRol=request.POST['insumos']
    clientesRol=request.POST['clientes']
    serviciosRol=request.POST['servicios']
    comprasRol=request.POST['compras']
    proveedoresRol=request.POST['proveedores']
    usuariosRol=request.POST['usuarios']
    citasRol=request.POST['citas']
    

    rol=Rol(nombre=nombreRol,configuracion=configuracionRol,insumos=insumosRol,clientes=clientesRol,servicios=serviciosRol,compras=comprasRol,proveedores=proveedoresRol,usuarios=usuariosRol,citas=citasRol)
    rol.save()
    return redirect("/listarRol/")

def formularioRol(request):       
    return render(request,"Configuracion/Crear-Rol.html")

def listarRol(request):   
    listarRol=Rol.objects.filter()  
    context={"crRol":listarRol}
    return render(request,"Configuracion/Configuracion.html",context)

def editarRol(request, id):    
    mostrar=Rol.objects.filter(idRol=id).first() 
    #ver=RolesPermisos.objects.filter(idRolesPermisos=id)   
    context={"mostrar":mostrar}
    return render(request,"Configuracion/Permisos.html",context)

def actualizarRol(request, id):      
    permisoRol=request.GET['Permiso']

    actualizar=Rol.objects.get(idRol=id)
    actualizar.permisoRol=permisoRol
    actualizar.save()

    return redirect("Rol")