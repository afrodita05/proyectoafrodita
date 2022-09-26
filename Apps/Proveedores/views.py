from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Proveedores.models import Proveedor

# Create your views here.
def CrearProveedor(request):
    EProveedor= request.POST['proveedor']
    telefonoProveedor= request.POST['telefono']
    nombreproveedor= request.POST['nombre']
    correoproveedor= request.POST['correo']
    direccionproveedor= request.POST['direccion']
    ORMProveedores=Proveedor(proveedor=EProveedor,telefono=telefonoProveedor,nombre=nombreproveedor,correo=correoproveedor,direccion=direccionproveedor)
    ORMProveedores.save()
    return redirect("Proveedor")

def FormularioAgregarProveedor(request):
    return render(request, 'Proveedores/Crear-Proveedor.html')

def ListarProveedor(request):
    LProveedor=Proveedor.objects.filter()
    context={"Lproveedor":LProveedor}
    return render(request,'Proveedores/Proveedores.html', context)


def EditarProveedor(request, idProveedor):
    EdiT=Proveedor.objects.filter(idProveedor=idProveedor).first()
    context={"EdiT":EdiT}
    return render(request,"Proveedores/Editar-Proveedor.html",context)

def ActualizarProveedor(request, idProveedor):
     nombreproveedor=request.GET['nombre']
     telefonoProveedor= request.GET['telefono']  
     correoproveedor= request.GET['correo']
     direccionproveedor= request.GET['direccion']
     ActualizarProveedor=Proveedor.objects.get(idProveedor=idProveedor)
     ActualizarProveedor.nombre=nombreproveedor
     ActualizarProveedor.telefono=telefonoProveedor
     ActualizarProveedor.correo=correoproveedor
     ActualizarProveedor.direccion=direccionproveedor
     ActualizarProveedor.save()
     return redirect ("Proveedor")

    