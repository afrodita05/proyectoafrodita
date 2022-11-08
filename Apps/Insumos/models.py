
from django.db import models
# Create your models here.

class Insumo(models.Model):
    idInsumo= models.AutoField(primary_key=True) 
    nombreInsumo = models.TextField(null= True, verbose_name='NombreInsumo')
    unidades = models.CharField(null= True, max_length=4, verbose_name='Unidades' )
    gramos = models.CharField(null= True, max_length=4, verbose_name='Gramos')