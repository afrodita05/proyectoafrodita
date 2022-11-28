import json
import random
from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from Apps.Compras.models import Compra, Detalle_Compra
from Apps.Insumos.models import Insumo 
from Apps.Proveedores.models import Proveedor
from django.contrib.auth.decorators import permission_required


@permission_required('Citas.view_citas',raise_exception=True) 
def CrearCompra(request):
    proveedor=Proveedor.objects.filter()
    insumo=Insumo.objects.filter()
    
    numeros="1234567890"
    longitud = 5
    unir = f"{numeros}"
    extension = random.sample(unir, longitud)
    codigoCompra = "".join(extension)
    
    
    
    data= json.loads(request.body)
    items = data["items"]
    VCompra=""
    ValorTotal = ""
    for item in items:
        proveedorCompra=item['proveedor']
        idProveedor = Proveedor.objects.filter(proveedor=proveedorCompra).values('idProveedor')[0]['idProveedor']
        VCompra = Compra(
            codigoCompra=codigoCompra,
            idProveedor_id=idProveedor,
            numeroFactura=item['numeroFactura'],
            fechaRecibo=item['fechaRecibo'],
            ValorTotal=item['ValorTotal'],
        )
        
    VCompra.save()
    
    idCompra=VCompra.idCompra
    for item in items:
        insumoCompra=item['insumo']
        
        idInsumo = Insumo.objects.filter(nombreInsumo=insumoCompra).values('idInsumo')[0]['idInsumo']
        DCompra=Detalle_Compra(
        idCompra_id=idCompra,
        idInsumo_id=idInsumo,
        cantidad=item['cantidad'],
        unidad = item['unidades'],
        costoUnidad=item['valorunidad'],
        subTotal=item['subtotal'],
        total=item['ValorTotal'],
        )
        DCompra.save()
        
        existenciasInsumo=Insumo.objects.filter(idInsumo=idInsumo).values_list('cantidad', flat=True).first()#Recoge el atributo "cantidad" de los insumos cuyo id sea igual al id almacenado en la variable "idInsumo"
        
        existenciasInsumo = int(existenciasInsumo)
        cantidadComprada =item['cantidad']
        cantidadComprada = int(cantidadComprada)
        nuevoInsumo = existenciasInsumo+cantidadComprada 

        insumoRecibido= Insumo.objects.get(idInsumo=idInsumo)

        insumoRecibido.cantidad = nuevoInsumo
        
        insumoRecibido.save()
        
    DTCompras=Detalle_Compra.objects.filter()
    idDTCompras = Detalle_Compra.objects.filter(idCompra_id=idCompra).values_list('idDetalle_Compra', flat=True)
    total = 0
    for DTCompras.idDetalle_Compra in idDTCompras:
        idDetalleCompra= DTCompras.idDetalle_Compra
        valorDTCompra= Detalle_Compra.objects.filter(idDetalle_Compra=idDetalleCompra).values_list('subTotal',flat= True).first()
        valorDTCompra = int(valorDTCompra)
        total=total+valorDTCompra
    actualizar=Compra.objects.get(idCompra=idCompra)
    actualizar.ValorTotal=total

    actualizar.save()
    return redirect("Compra")

@permission_required('Citas.view_citas',raise_exception=True) 
def FormularioAgregarInsumo(request):
    return render (request, 'Compras/Crear-Insumo.html')

@permission_required('Citas.view_citas',raise_exception=True) 
def CrearInsumo (request):
    nInsumo = request.POST['txtNombre']
    tipoUnidad = request.POST['tipoUnidad']
    errorI= []
    errorInsO= []
    if Insumo.objects.filter(nombreInsumo= nInsumo).exists():
        errorI.append(1)
        contex={"errorI": errorI}
        return render(request,'Compras/Crear-Insumo.html',contex)
        
    elif nInsumo == (''):
        errorInsO.append(1)
        contex={"errorInsO": errorInsO}
        return render(request,'Compras/Crear-Insumo.html',contex)
    
    else:
        insumo = Insumo(nombreInsumo = nInsumo, tipoUnidad = tipoUnidad)
        errorI.clear()
        insumo.save()
    return redirect('/FormularioAgregarCompra/')

#def CrearInsumo (request):
#    nombreInsumo = request.POST['txtNombre']
#    insumo = Insumo.objects.create(nombreInsumo =nombreInsumo)
#    return redirect('/FormularioAgregarCompra/')

@permission_required('Citas.view_citas',raise_exception=True) 
def FormularioAgregarCompra(request):
    proveedor=Proveedor.objects.filter()
    nombreInsumo=Insumo.objects.filter()
    context={"proveedor":proveedor,"nombreInsumo":nombreInsumo}   
    return render(request,'Compras/Crear-Compra.html', context)

@permission_required('Citas.view_citas',raise_exception=True) 
def ListarCompra(request):
    LCompra=Compra.objects.filter()
    
    context={"Lcompra":LCompra}
    return render(request,'Compras/Compras.html', context)

@permission_required('Citas.view_citas',raise_exception=True) 
def DetalleCompras(request, id):
    DTCompras=Detalle_Compra.objects.filter(idCompra_id=id).first
    idDTCompras = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idDetalle_Compra', flat=True)
    Insumos = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idInsumo', flat= True) 
    Cantidad = Detalle_Compra.objects.filter(idCompra_id =id).values_list('cantidad', flat= True)
    
    idInsumos = Detalle_Compra.objects.filter(idCompra_id=id,idInsumo__in=Insumos)
    
    cantidadI = Detalle_Compra.objects.filter(idCompra_id=id,cantidad__in=Insumos)
    context={"DTCompras":DTCompras, "idInsumo":idInsumos, "cantidad":cantidadI}
    return render(request,"Compras/Ver-Detalle.html",context) 

@permission_required('Citas.view_citas',raise_exception=True)
def estadoCompra(request, id):
   estadoCompra = Compra.objects.get( idCompra = id)
   return render(request,'Compras/estado.html', {'estadoCompra':estadoCompra})

@permission_required('Citas.view_citas',raise_exception=True)
def estadocompra (request, id):
    idCompra = request.POST['id']
    estadoC = request.POST['EstadoC']
    compra = Compra.objects.get(idCompra = id)
    
    compra.estadoC = estadoC
    compra.save()
    return redirect('Compra')

@permission_required('Citas.view_citas',raise_exception=True)
def EliminarCompra(request, id):   
    ECompra=Compra.objects.get(idCompra=id)
    ECompra.delete() 
    return redirect("Compra")

