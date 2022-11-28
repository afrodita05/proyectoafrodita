from math import perm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import Group, Permission
from Apps.Configuracion.models import Rol
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('auth.view_group',raise_exception=True) 
def crearRol(request): 
         
    nombreRol=request.POST['nombre']
    lPerm=['Configuracion','Insumos','Clientes','Servicios','Compras','Proveedores','Usuarios','Citas']
    

    rol = Group() #Crea un grupo con la variable "rol"
    rol.name= nombreRol #Toma el contenido del input "nombre" introducido por el usuario y lo asigna como nombre del rol
    rol.save() #Guarda el nuevo rol
    

    if request.method=='POST':
        permisos=request.POST.getlist('permisos')
        
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

        agregar_rol= Permission.objects.get(name='Can add group')
        ver_rol= Permission.objects.get(name='Can view group') 
        cambiar_rol= Permission.objects.get(name='Can change group')
        eliminar_rol= Permission.objects.get(name='Can delete group')
        rol.permissions.add(agregar_rol, ver_rol, cambiar_rol, eliminar_rol)
    

    if compInsu>0:

        agregar_insumo= Permission.objects.get(name='Can add insumo')
        ver_insumo= Permission.objects.get(name='Can view insumo') #Toma el permiso "puede ver insumo", y lo asigna a la variable ver_insumo
        cambiar_insumo= Permission.objects.get(name='Can change insumo')
        eliminar_insumo= Permission.objects.get(name='Can delete insumo')
        #Hace lo mismo con editar y eliminar.
        rol.permissions.add(agregar_insumo,ver_insumo, cambiar_insumo, eliminar_insumo)


    if compClien>0:
        
        #Clientes
        agregar_cliente= Permission.objects.get(name='Can add clientes')
        ver_cliente= Permission.objects.get(name='Can view clientes') 
        cambiar_cliente= Permission.objects.get(name='Can change clientes')
        eliminar_cliente= Permission.objects.get(name='Can delete clientes')

        rol.permissions.add(agregar_cliente,ver_cliente, cambiar_cliente, eliminar_cliente)


    if compServ>0:
        agregar_servicio= Permission.objects.get(name='Can add servicios')
        ver_servicio= Permission.objects.get(name='Can view servicios') 
        cambiar_servicio= Permission.objects.get(name='Can change servicios')
        eliminar_servicio= Permission.objects.get(name='Can delete servicios')
        rol.permissions.add(agregar_servicio,ver_servicio, cambiar_servicio, eliminar_servicio)
        

    if compCompr>0:
        agregar_compra= Permission.objects.get(name='Can add compra')
        ver_compra= Permission.objects.get(name='Can view compra') 
        cambiar_compra= Permission.objects.get(name='Can change compra')
        agregar_dtcompra= Permission.objects.get(name='Can add detalle_ compra')
        cambiar_dtcompra= Permission.objects.get(name='Can change detalle_ compra')
        ver_dtcompra= Permission.objects.get(name='Can view detalle_ compra')

        rol.permissions.add(agregar_compra,ver_compra, cambiar_compra,agregar_dtcompra,cambiar_dtcompra,ver_dtcompra)
        

    if compProv>0:

        agregar_proveedor= Permission.objects.get(name='Can add proveedor')
        ver_proveedor= Permission.objects.get(name='Can view proveedor') 
        cambiar_proveedor= Permission.objects.get(name='Can change proveedor')
        eliminar_proveedor= Permission.objects.get(name='Can delete proveedor')
        rol.permissions.add(agregar_proveedor,ver_proveedor, cambiar_proveedor, eliminar_proveedor)
    

    if compUsua>0:
        agregar_usuario= Permission.objects.get(name='Can add user')
        ver_usuario= Permission.objects.get(name='Can view user') 
        cambiar_usuario= Permission.objects.get(name='Can change user')
        eliminar_usuario= Permission.objects.get(name='Can delete user')
        rol.permissions.add(agregar_usuario,ver_usuario, cambiar_usuario, eliminar_usuario)


    if compCita>0:

        agregar_citas= Permission.objects.get(name='Can add citas')
        ver_citas= Permission.objects.get(name='Can view citas') 
        cambiar_citas= Permission.objects.get(name='Can change citas')
        eliminar_citas= Permission.objects.get(name='Can delete citas')
        rol.permissions.add(agregar_citas,ver_citas, cambiar_citas, eliminar_citas)
       

    
    return redirect("/listarRol/")

@permission_required('auth.view_group',raise_exception=True)  

def editarRol(request, id):
    mostrar=Group.objects.filter(id=id).first()
    context={"mostrar":mostrar}
    return render(request,"Configuracion/Editar-Rol.html",context)

@permission_required('auth.view_group',raise_exception=True) 

def formularioRol(request):    
    return render(request,"Configuracion/Crear-Rol.html")

@permission_required('auth.view_group',raise_exception=True) 

def listarRol(request):   
    
    listarRol=Group.objects.filter()       

    context={"crRol":listarRol}
    return render(request,"Configuracion/Configuracion.html",context)


@permission_required('auth.view_group',raise_exception=True) 

def actualizarRol(request, id):      
    nombreRol=request.GET['nombre']
    actualizar=Group.objects.get(id=id)
    actualizar.name= nombreRol
    actualizar.save()
    actualizar.permissions.clear()
    if request.method=='GET':
        permisos=request.GET.getlist('permisos')
        
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

@permission_required('auth.view_group',raise_exception=True) 

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
    contexto={"mostrar":mostrar,"rol":rol,"usuario":usuario,"proveedor":proveedor,"compras":compras,"insumos":insumos,"servicio":servicio,"cliente":cliente,"cita":cita, "listaP":listaP}
    return render(request,"Configuracion/Detalle-Rol.html",contexto)