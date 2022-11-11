from django.db import models        
from Apps.Proveedores.models import Proveedor
<<<<<<< HEAD

=======
from Apps.Insumos.models import Insumo
>>>>>>> 7b4a5018eefa1eb68f4c2fc8e09ab0ed29669771
# Create your models here.


class Compra(models.Model):
    idCompra=models.AutoField(primary_key=True)
    codigoCompra=models.CharField(max_length=10)
    idProveedor=models.ForeignKey(Proveedor, related_name='Compra', on_delete=models.PROTECT, null=True)
    numeroFactura=models.CharField(max_length=60)
    fechaRecibo=models.DateTimeField(auto_now_add=True)
    ValorTotal=models.CharField(max_length=10)

    
class Detalle_Compra(models.Model):
    idDetalle_Compra=models.AutoField(primary_key=True)
    idCompra=models.ForeignKey(Compra, on_delete=models.PROTECT) 
    idInsumo=models.ForeignKey('Insumos.Insumo', on_delete=models.PROTECT) 
    cantidad = models.IntegerField(null= True)
    tipoUnidad = models.CharField(max_length=14, null = True)
    costoUnidad = models.IntegerField(null= True)
    subTotal = models.IntegerField(null= True)
    total = models.IntegerField(null = True)