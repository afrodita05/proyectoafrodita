from math import perm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import Group, Permission
from Apps.Configuracion.models import Rol
# Create your views here.

def crearRol(request): 
         
    nombreRol=request.POST['nombre']
    lPerm=['Configuracion','Insumos','Clientes','Servicios','Compras','Proveedores','Usuarios','Citas']
    

    rol = Group() #Crea un grupo con la variable "rol"
    rol.name= nombreRol #Toma el contenido del input "nombre" introducido por el usuario y lo asigna como nombre del rol
    rol.save() #Guarda el nuevo rol
    

    if request.method=='POST':
        permisos=request.POST.getlist('permisos')
        print(permisos)
        
    compConf= permisos.count("Configuracion")
    compInsu= permisos.count("Insumos")
    compClien= permisos.count("Clientes")
    compServ= permisos.count("Servicios")
    compCompr= permisos.count("Compras")
    compProv= permisos.count("Proveedores")
    compUsua= permisos.count("Usuarios")
    compCita= permisos.count("Citas")
    configuracionRol= None 
    comprasRol= None
    insumosRol= None
    clientesRol= None
    serviciosRol= None
    proveedoresRol= None
    usuariosRol= None
    citasRol= None
    

    if compConf>0:

        ver_rol= Permission.objects.get(name='Can view group') 
        
        rol.permissions.add(ver_rol)
    

    if compInsu>0:

       
        ver_insumo= Permission.objects.get(name='Can view insumo') #Toma el permiso "puede ver insumo", y lo asigna a la variable ver_insumo
        
        rol.permissions.add(ver_insumo)


    if compClien>0:
        
       
        ver_cliente= Permission.objects.get(name='Can view clientes') 
        

        rol.permissions.add(ver_cliente)
      

    if compServ>0:
    
        ver_servicio= Permission.objects.get(name='Can view servicios') 
       
        rol.permissions.add(ver_servicio)
        

    if compCompr>0:
      
        ver_compra= Permission.objects.get(name='Can view compra') 
        

        rol.permissions.add(ver_compra)
        

    if compProv>0:

       
        ver_proveedor= Permission.objects.get(name='Can view proveedor') 
        
        rol.permissions.add(ver_proveedor)
    

    if compUsua>0:
       
        ver_usuario= Permission.objects.get(name='Can view user') 
        
        rol.permissions.add(ver_usuario)


    if compCita>0:

       
        ver_citas= Permission.objects.get(name='Can view citas') 
       
        rol.permissions.add(ver_citas)
       

    
    return redirect("/listarRol/")

def editarRol(request, id):
    mostrar=Group.objects.filter(id=id).first()
    print(mostrar)
    context={"mostrar":mostrar}
    return render(request,"Configuracion/Editar-Rol.html",context)

def formularioRol(request):    
    print(request.user.id)   
    return render(request,"Configuracion/Crear-Rol.html")

def listarRol(request):   
    current_user=request.user
    print(current_user.id)
    listarRol=Group.objects.filter()       

    context={"crRol":listarRol}
    return render(request,"Configuracion/Configuracion.html",context)


def actualizarRol(request, id):      
    nombreRol=request.GET['nombre']
    actualizar=Group.objects.get(id=id)
    actualizar.name= nombreRol
    actualizar.save()
    actualizar.permissions.clear()
    if request.method=='GET':
        permisos=request.GET.getlist('permisos')
        print(permisos, "AAAAAAAAAAA")
        
    compConf= permisos.count("Configuracion")
    compInsu= permisos.count("Insumos")
    compClien= permisos.count("Clientes")
    compServ= permisos.count("Servicios")
    compCompr= permisos.count("Compras")
    compProv= permisos.count("Proveedores")
    compUsua= permisos.count("Usuarios")
    compCita= permisos.count("Citas")
    configuracionRol= None 
    comprasRol= None
    insumosRol= None
    clientesRol= None
    serviciosRol= None
    proveedoresRol= None
    usuariosRol= None
    citasRol= None
    

    if compConf>0:

        ver_rol= Permission.objects.get(name='Can view group') 
        
        actualizar.permissions.add(ver_rol)
    

    if compInsu>0:

       
        ver_insumo= Permission.objects.get(name='Can view insumo') #Toma el permiso "puede ver insumo", y lo asigna a la variable ver_insumo
        
        actualizar.permissions.add(ver_insumo)


    if compClien>0:
        
       
        ver_cliente= Permission.objects.get(name='Can view clientes') 
        

        actualizar.permissions.add(ver_cliente)
      

    if compServ>0:
    
        ver_servicio= Permission.objects.get(name='Can view servicios') 
       
        actualizar.permissions.add(ver_servicio)
        

    if compCompr>0:
      
        ver_compra= Permission.objects.get(name='Can view compra') 
        

        actualizar.permissions.add(ver_compra)
        

    if compProv>0:

       
        ver_proveedor= Permission.objects.get(name='Can view proveedor') 
        
        actualizar.permissions.add(ver_proveedor)
    

    if compUsua>0:
       
        ver_usuario= Permission.objects.get(name='Can view user') 
        
        actualizar.permissions.add(ver_usuario)


    if compCita>0:

       
        ver_citas= Permission.objects.get(name='Can view citas') 
       
        actualizar.permissions.add(ver_citas)
       


    return redirect("/listarRol/")

def detalleRol(request,id):
    rol= " "
    usuario= ""
    proveedor=" "
    compras = ""
    insumos = ""
    servicio = " "
    cliente = " "
    cita = " "
    mostrar=Group.objects.filter(id=id).first()
    permisosRol= Group.objects.get(id=id).permissions.filter(name__contains="group")
    permisosUsuario= Group.objects.get(id=id).permissions.filter(name__contains="user")
    permisosProveedor= Group.objects.get(id=id).permissions.filter(name__contains="proveedor")
    permisosCompra= Group.objects.get(id=id).permissions.filter(name__contains="compra")
    permisosInsumo= Group.objects.get(id=id).permissions.filter(name__contains="insumo")
    permisosServicio= Group.objects.get(id=id).permissions.filter(name__contains="servicios")
    permisosCliente= Group.objects.get(id=id).permissions.filter(name__contains="cliente")
    permisosCitas= Group.objects.get(id=id).permissions.filter(name__contains="citas")
    
    listaP=[]
    
    if permisosRol:
        rol = "Roles"
        listaP.append(rol)
    if permisosUsuario:
        usuario = "Usuarios"
        listaP.append(usuario)
    if permisosProveedor:
        proveedor= "Proveedores"
        listaP.append(proveedor)
    if permisosCompra:
        compras = "Compras"
        listaP.append(compras)
    if permisosInsumo:
        insumos = "Insumos"
        listaP.append(insumos)
    if permisosServicio: 
        servicio = "Servicio"
        listaP.append(servicio)
    if permisosCliente:
        cliente = "Clientes"
        listaP.append(cliente)
    if permisosCitas:
        cita = "Citas"
        listaP.append(cita)
    print(listaP)
    contexto={"mostrar":mostrar,"rol":rol,"usuario":usuario,"proveedor":proveedor,"compras":compras,"insumos":insumos,"servicio":servicio,"cliente":cliente,"cita":cita, "listaP":listaP}
    return render(request,"Configuracion/Detalle-Rol.html",contexto)