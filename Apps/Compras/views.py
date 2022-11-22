import json
import random
from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect

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
    
    numeros="1234567890"
    longitud = 5
    unir = f"{numeros}"
    extension = random.sample(unir, longitud)
    codigoCompra = "".join(extension)
    
    
    
    data= json.loads(request.body)
    items = data["items"]
    print(items,type(items))
    VCompra=""
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
        
        print (insumoCompra)
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
    idDTCompras = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idDetalle_Compra', flat=True)
    Insumos = Detalle_Compra.objects.filter(idCompra_id=id).values_list('idInsumo', flat= True) 
    Cantidad = Detalle_Compra.objects.filter(idCompra_id =id).values_list('cantidad', flat= True)
    print (Insumos,'zzz')
    idInsumos = Detalle_Compra.objects.filter(idCompra_id=id,idInsumo__in=Insumos)
    print(idInsumos, 'hola')
    cantidadI = Detalle_Compra.objects.filter(idCompra_id=id,cantidad__in=Insumos)
    context={"DTCompras":DTCompras, "idInsumo":idInsumos, "cantidad":cantidadI}
    print (idDTCompras)
    return render(request,"Compras/Ver-Detalle.html",context) 

def estadoCompra(request, id):
   estadoCompra = Insumo.objects.get(estado= id)
   return render(request,'Compras/estado.html', {'estadoCompra':estadoCompra})

def esatdocompra (request):
    idCompra = request.POST['id']
    estadoC = request.POST['EstadoC']
    compra = Insumo.objects.get(idCompra = idCompra)
    compra.estadoC = estadoC
    compra.save()
    return redirect('Compra')

def EliminarCompra(request, id):   
    ECompra=Compra.objects.get(idCompra=id)
    ECompra.delete() 
    return redirect("Compra")

