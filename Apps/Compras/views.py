from multiprocessing import context
import json
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Compras.models import Compra, Detalle_Compra
from Apps.Insumos.models import Insumo
# Create your views here.

def CrearCompra(request):
    data= json.loads(request.body)
    items = data["items"]
    print(items,type(items))
    VCompra=""
    for item in items:
        VCompra = Compra(
            codigoCompra=item['codigoCompra'],
            proveedor=item['proveedor'],
            numeroFactura=item['numeroFactura'], 
            fechaRecibo=item['fechaRecibo'],
            ValorTotal=item['ValorTotal']
        )
    VCompra.save()
    idCompra=VCompra.idCompra
    for item in items:
        nuevoInsumo=Insumo(
            nombre=item['insumo'], 
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



def FormularioAgregarCompra(request):
    return render(request, 'Compras/Crear-Compra.html')

def ListarCompra(request):
    LCompra=Compra.objects.filter()
    context={"Lcompra":LCompra}
    return render(request,'Compras/Compras.html', context)

def DetalleCompras(request, id):
    DTCompras=Detalle_Compra.objects.filter(idDetalle_Compra=id).first()  
    idCompras = Detalle_Compra.objects.filter(idDetalle_Compra=id).values('idCompra_id')[0]['idCompra_id']
    objetos=Insumo.objects.filter(idCompra_id=idCompras)
    objetosNombre=Insumo.objects.filter(idCompra_id=idCompras).values('insumo')
    context={"DTCompras":DTCompras,"objetos":objetos,"idCompras":idCompras,"objetosNombre":objetosNombre}
    return render(request,"Compras/Ver-Detalle.html",context) 

   
def EliminarCompra(request, id):   
    ECompra=Compra.objects.get(idCompra=id)
    ECompra.delete() 
    return redirect("Compra")

def ListarInsumos(request):
    pass

