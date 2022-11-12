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
        
        #Historial corporal

        agregar_corporal= Permission.objects.get(name='Can add estetico corporal')
        ver_corporal= Permission.objects.get(name='Can view estetico corporal') 
        cambiar_corporal= Permission.objects.get(name='Can change estetico corporal')
        
        rol.permissions.add(agregar_corporal,ver_corporal, cambiar_corporal)

        #Historial facial
        
        agregar_facial= Permission.objects.get(name='Can add estetico facial')
        ver_facial= Permission.objects.get(name='Can view estetico facial') 
        cambiar_facial= Permission.objects.get(name='Can change estetico facial')
        
        rol.permissions.add(agregar_facial,ver_facial, cambiar_facial)

        #Sesiones

        agregar_sesiones= Permission.objects.get(name='Can add sesiones')     
        ver_sesiones= Permission.objects.get(name='Can view sesiones') 
        cambiar_sesiones= Permission.objects.get(name='Can change sesiones')   

        rol.permissions.add(agregar_sesiones,ver_sesiones, cambiar_sesiones)

        #Control Medidas
        
        agregar_control= Permission.objects.get(name='Can add control medidas')     
        ver_control= Permission.objects.get(name='Can view control medidas') 
        cambiar_control= Permission.objects.get(name='Can change control medidas')   

        rol.permissions.add(agregar_control,ver_control, cambiar_control)


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
       

    rol= Rol(nombre=nombreRol,configuracion=configuracionRol,insumos=insumosRol,clientes=clientesRol,servicios=serviciosRol,compras=comprasRol,proveedores=proveedoresRol,usuarios=usuariosRol,citas=citasRol)
    rol.save()
    
    return redirect("/listarRol/")

def pruebaRol(request): 
         
    #grupito = Group.objects.create(name="grupito")
    grupito = Group()
    grupito.name= "Grupitososos" #request.POST['nombreRol'], hacer en página de creación.
    grupito.save()
    ver_insumo= Permission.objects.get(name='Can view insumo')  
    grupito.permissions.add(ver_insumo)
    return redirect("/listarRol/")

def formularioRol(request):       
    return render(request,"Configuracion/Crear-Rol.html")

def listarRol(request):   
    listarRol=Group.objects.filter()
    # idRol= listarRol.id 
    # permisosAsociados= Group.permissions.objects.filter(group_id=idRol).values_list('permission_id', flat=True)
    # print(permisosAsociados)
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