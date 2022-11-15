
from django.db import models
# Create your models here.

class Insumo(models.Model):
    idInsumo= models.AutoField(primary_key=True)
    nombreInsumo = models.TextField(null= True, verbose_name='Insumo')
    cantidad = models.IntegerField(default= 0, verbose_name='Cantidad')
    tipoUnidad = models.CharField(max_length=14, null = True)
    estado = models.BooleanField(default= True, verbose_name='Estado')
