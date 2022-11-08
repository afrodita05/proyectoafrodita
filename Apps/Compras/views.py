from multiprocessing import context
import json
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Compras.models import Compra, Detalle_Compra
from Apps.Insumos.models import Insumo
from Apps.Proveedores.models import Proveedor
# Create your views here.

def CrearCompra(request):
    proveedor=Proveedor.objects.filter()
    insumo=Insumo.objects.filter()
    data= json.loads(request.body)
    items = data["items"]
    print(items,type(items))
    VCompra=""
    for item in items:
        proveedorCompra=item['proveedor'] 
        idProveedor = Proveedor.objects.filter(proveedor=proveedorCompra).values('idProveedor')[0]['idProveedor']
        insumoCompra=item['insumo']
        idInsumo = Insumo.objects.filter(nombreInsumo=insumoCompra).values('idInsumo')[0]['idInsumo']
        VCompra = Compra(
            codigoCompra=item['codigoCompra'],
            idProveedor_id=idProveedor,
            idInsumo_id=idInsumo,
            numeroFactura=item['numeroFactura'], 
            fechaRecibo=item['fechaRecibo'],
            ValorTotal=item['ValorTotal']
        )
    VCompra.save()
    
    idCompra=VCompra.idCompra
    for item in items:
        nuevoInsumo=Insumo(
            cantidad=item['cantidad'],
        )
        nuevoInsumo.save()

        idInsumo=nuevoInsumo.idInsumo

        DCompra=Detalle_Compra(
        idCompra_id=idCompra,
        idInsumo_id=idInsumo
        )
        DCompra.save()

    return redirect("Compra")

    #for item in items:
    #    nuevoInsumo=Insumo(
    #        cantidad=item['cantidad'],
    #    )
    #    nuevoInsumo.save()
#
    #    idInsumo=nuevoInsumo.idInsumo

    #    DCompra=Detalle_Compra(
        #idCompra_id=idCompra,
     #   idInsumo_id=idInsumo
    #   )
    # DCompra.save()
    #return redirect("Compra")

def FormularioAgregarInsumo(request):
    return render (request, 'Compras/Crear-Insumo.html')


def CrearInsumo (request):
    nombreInsumo = request.POST['txtNombre']
    insumo = Insumo.objects.create(nombreInsumo =nombreInsumo)
    return redirect('/FormularioAgregarCompra/')

def FormularioAgregarCompra(request):
    proveedor=Proveedor.objects.filter()
    nombreInsumo=Insumo.objects.filter()
    context={"proveedor":proveedor,"nombreInsumo":nombreInsumo}   
    return render(request, 'Compras/Crear-Compra.html', context)

def ListarCompra(request):
    LCompra=Compra.objects.filter()
    context={"Lcompra":LCompra}
    return render(request,'Compras/Compras.html', context)

def DetalleCompras(request, id):
    DTCompras=Detalle_Compra.objects.filter(idCompra_id=id).first

    idDTCompras = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idDetalle_Compra', flat=True) #Obtener id de los DT compra basados en la id de compra
    
    idInsumos=Insumo.objects.filter(idInsumo__in=idDTCompras) #buscar los insumos que compartan el id de detalle de compra

    context={"DTCompras":DTCompras, "idInsumo":idInsumos}
    return render(request,"Compras/Ver-Detalle.html",context) 

   
def EliminarCompra(request, id):   
    ECompra=Compra.objects.get(idCompra=id)
    ECompra.delete() 
    return redirect("Compra")



