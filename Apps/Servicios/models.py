from django.db import models

# Create your models here.

class Servicios(models.Model):
    #PASO 1:
    #Añadir costo del servicio
    idServicio=models.AutoField(primary_key=True)
    nServicio=models.CharField(max_length=50)
    tiempo= models.IntegerField()
    valor=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return '{}'.format(self.nServicio)
    

class Servicios_Insumo(models.Model):
    idServicios_Insumo= models.AutoField(primary_key=True)
    idServicio= models.ForeignKey(Servicios, on_delete=models.PROTECT) 
    idInsumo= models.ForeignKey('Insumos.Insumo', on_delete=models.PROTECT)
    cantidadUsada = models.IntegerField(default=0) 
