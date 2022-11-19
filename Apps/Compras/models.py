from django.db import models        
from Apps.Proveedores.models import Proveedor
from Apps.Insumos.models import Insumo

class Compra(models.Model):
    idCompra=models.AutoField(primary_key=True)
    codigoCompra=models.CharField(max_length=10)
    idProveedor=models.ForeignKey(Proveedor, related_name='Compra', on_delete=models.PROTECT, null=True)
    numeroFactura=models.CharField(max_length=60)
    fechaRecibo=models.DateTimeField(auto_now_add=True)
    ValorTotal=models.FloatField(max_length=10)

    
class Detalle_Compra(models.Model):
    idDetalle_Compra=models.AutoField(primary_key=True)
    idCompra=models.ForeignKey(Compra, on_delete=models.PROTECT) 
    idInsumo=models.ForeignKey('Insumos.Insumo', on_delete=models.PROTECT) 
    cantidad = models.IntegerField(null= True)
    unidad= models.IntegerField(null = True)
    costoUnidad = models.FloatField(null= True)
    subTotal = models.FloatField(null= True)
    total = models.FloatField(null = True)