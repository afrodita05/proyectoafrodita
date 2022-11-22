from multiprocessing import context
import json
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Compras.models import Compra, Detalle_Compra
from Apps.Insumos.models import Insumo
from Apps.Proveedores.models import Proveedor
from django.contrib.auth.decorators import permission_required
# Create your views here.

@permission_required('Compras.view_compra') 
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
        VCompra = Compra(
            codigoCompra=item['codigoCompra'],
            idProveedor_id=idProveedor,
            numeroFactura=item['numeroFactura'], 
            fechaRecibo=item['fechaRecibo'],
            ValorTotal=item['ValorTotal']
        )
    VCompra.save()
    idCompra=VCompra.idCompra
    for item in items:
        insumoCompra=item['insumo']
        print (insumoCompra)
        idInsumo = Insumo.objects.filter(nombreInsumo=insumoCompra).values('idInsumo')[0]['idInsumo']
        
        DCompra=Detalle_Compra(
        idCompra_id=idCompra,
        idInsumo_id=idInsumo,
        cantidad=item['cantidad'],
        tipoUnidad=item['tipoUnidad'],
        costoUnidad=item['valorunidad'],
        subTotal=item['ValorTotalInsumo'],
        total=item['ValorTotal'],
        )
        
        print( Detalle_Compra.idInsumo_id, 'xx', idInsumo)
        DCompra.save()
        
        existenciasInsumo=Insumo.objects.filter(idInsumo=idInsumo).values_list('cantidad', flat=True).first()#Recoge el atributo "cantidad" de los insumos cuyo id sea igual al id almacenado en la variable "idInsumo"
        existenciasInsumo = int(existenciasInsumo)
        print (existenciasInsumo, 'exiss')
        cantidadComprada =item['cantidad']
        cantidadComprada = int(cantidadComprada)
        print (cantidadComprada, 'cantidddddd')
        nuevoInsumo = existenciasInsumo+cantidadComprada 

        insumoRecibido= Insumo.objects.get(idInsumo=idInsumo)

        insumoRecibido.cantidad = nuevoInsumo
        
        insumoRecibido.save()
        
    return redirect("Compra")

@permission_required('Compras.view_compra') 
def FormularioAgregarInsumo(request):
    return render (request, 'Compras/Crear-Insumo.html')

@permission_required('Compras.view_compra') 
def CrearInsumo (request):
    nombreInsumo = request.POST['txtNombre']
    insumo = Insumo.objects.create(nombreInsumo =nombreInsumo)
    return redirect('/FormularioAgregarCompra/')

@permission_required('Compras.view_compra') 
def FormularioAgregarCompra(request):
    proveedor=Proveedor.objects.filter()
    nombreInsumo=Insumo.objects.filter()
    context={"proveedor":proveedor,"nombreInsumo":nombreInsumo}   
    return render(request,'Compras/Crear-Compra.html', context)

@permission_required('Compras.view_compra') 
def ListarCompra(request):
    LCompra=Compra.objects.filter()
    print(LCompra)
    context={"Lcompra":LCompra}
    return render(request,'Compras/Compras.html', context)

@permission_required('Compras.view_compra') 
def DetalleCompras(request, id):
    DTCompras=Detalle_Compra.objects.filter(idCompra_id=id).first
    idDTCompras = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idDetalle_Compra', flat=True) #Obtener id de los DT compra basados en la id de compra
    Insumos = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idInsumo', flat= True) #buscar los insumos que compartan el id de detalle de compra
    Cantidad = Detalle_Compra.objects.filter(idCompra_id =id).values_list('cantidad', flat= True)
    print (Insumos,'zzz')
    idInsumos = Detalle_Compra.objects.filter(idCompra_id=id,idInsumo__in=Insumos)
    print(idInsumos, 'hola')
    cantidadI = Detalle_Compra.objects.filter(idCompra_id=id,cantidad__in=Insumos)
    context={"DTCompras":DTCompras, "idInsumo":idInsumos, "cantidad":cantidadI}
    print (idDTCompras)
    return render(request,"Compras/Ver-Detalle.html",context) 

@permission_required('Compras.view_compra') 
def EliminarCompra(request, id):   
    ECompra=Compra.objects.get(idCompra=id)
    ECompra.delete() 
    return redirect("Compra")