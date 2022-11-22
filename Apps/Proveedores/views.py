from django.shortcuts import render, redirect
from Apps.Proveedores.models import Proveedor
from Apps.Proveedores.forms import *

# Create your views here.
def CrearProveedor(request):

    if request.method=='POST':
        formulario_proveedor=FormularioProveedor(request.POST)
        if formulario_proveedor.is_valid():
            formulario_proveedor.save()
            return redirect('Proveedor')
    else: 
        formulario_proveedor=FormularioProveedor()
    contexto={'formulario_proveedor':formulario_proveedor}
    return render(request,'Proveedores/Crear-Proveedor.html',contexto)
    
    
    
def EditarProveedor(request, id):
    proveedor=Proveedor.objects.get(idProveedor=id)
    if request.method=='GET':
        formulario_proveedor=FormularioProveedor(instance=proveedor)
    else:
        formulario_proveedor=FormularioProveedor(request.POST,instance=proveedor)
        if formulario_proveedor.is_valid():
            formulario_proveedor.save()
            return redirect('Proveedor')
    contexto={'formulario_proveedor':formulario_proveedor}
    
    return render(request,'Proveedores/Editar-Proveedor.html',contexto)

# def FormularioAgregarProveedor(request):
#     return render(request, 'Proveedores/Crear-Proveedor.html')

def ListarProveedor(request):
    LProveedor=Proveedor.objects.filter()
    context={"Lproveedor":LProveedor}
    return render(request,'Proveedores/Proveedores.html', context)




# def EditarProveedor(request, idProveedor):
#     EdiT=Proveedor.objects.filter(idProveedor=idProveedor).first()
#     context={"EdiT":EdiT}
#     return render(request,"Proveedores/Editar-Proveedor.html",context)

# def ActualizarProveedor(request, idProveedor):
#      nombreproveedor=request.GET['nombre']
#      telefonoProveedor= request.GET['telefono']  
#      correoproveedor= request.GET['correo']
#      direccionproveedor= request.GET['direccion']
#      empresaproveedor= request.GET['proveedor']
#      ActualizarProveedor=Proveedor.objects.get(idProveedor=idProveedor)
#      ActualizarProveedor.nombre=nombreproveedor
#      ActualizarProveedor.telefono=telefonoProveedor
#      ActualizarProveedor.correo=correoproveedor
#      ActualizarProveedor.direccion=direccionproveedor
#      ActualizarProveedor.proveedor=empresaproveedor
#      ActualizarProveedor.save()
#      return redirect ("Proveedor")

    