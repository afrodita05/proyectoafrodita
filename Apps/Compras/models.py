from django.db import models        
from Apps.Proveedores.models import Proveedor
from Apps.Insumos.models import Insumo

class Compra(models.Model):
    idCompra=models.AutoField(primary_key=True)
    codigoCompra=models.CharField(max_length=10)
    idProveedor=models.ForeignKey(Proveedor, related_name='Compra', on_delete=models.PROTECT, null=True)
    numeroFactura=models.CharField(max_length=60)
    fechaRecibo=models.DateTimeField(auto_now_add=True)
    ValorTotal=models.CharField(max_length=14)
    estadoC = models.BooleanField(default= True, verbose_name='Estado')

    
class Detalle_Compra(models.Model):
    idDetalle_Compra=models.AutoField(primary_key=True)
    idCompra=models.ForeignKey(Compra, on_delete=models.PROTECT) 
    idInsumo=models.ForeignKey('Insumos.Insumo', on_delete=models.PROTECT) 
    cantidad = models.IntegerField(null= True)
    unidad= models.IntegerField(null = True)
    costoUnidad = models.FloatField(null= True)
    subTotal = models.CharField(null= True, max_length=14)
    total = models.CharField(null = True, max_length=14)