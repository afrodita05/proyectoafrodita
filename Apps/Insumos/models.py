
from django.db import models
# Create your models here.

class Insumo(models.Model):
<<<<<<< HEAD
    idInsumo= models.AutoField(primary_key=True) 
    nombreInsumo = models.TextField(null= True, verbose_name='NombreInsumo')
    unidades = models.CharField(null= True, max_length=4, verbose_name='Unidades' )
    gramos = models.CharField(null= True, max_length=4, verbose_name='Gramos')
=======
    idInsumo= models.AutoField(primary_key=True)
    nombreInsumo = models.TextField(null= True, verbose_name='Insumo')
    cantidad = models.IntegerField(default= 0, verbose_name='Cantidad')
    tipoUnidad = models.CharField(max_length=14, null = True)
>>>>>>> 7b4a5018eefa1eb68f4c2fc8e09ab0ed29669771
