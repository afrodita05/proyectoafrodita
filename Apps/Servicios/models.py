from django.db import models

# Create your models here.

class Servicios(models.Model):
    idServicio=models.AutoField(primary_key=True)
    nServicio=models.CharField(max_length=50)
    tiempo= models.IntegerField()

class Servicios_Insumo(models.Model):
    idServicios_Insumo= models.AutoField(primary_key=True)
    idServicio= models.ForeignKey(Servicios, on_delete=models.PROTECT) 
    idInsumo= models.ForeignKey('Insumos.Insumo', on_delete=models.PROTECT) 
