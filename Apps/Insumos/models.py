
from django.db import models
# Create your models here.

class Insumo(models.Model):
    idInsumo= models.AutoField(primary_key=True) 
    nombreInsumo = models.TextField(null= True, verbose_name='Insumo')
    cantidad = models.CharField(null= True, max_length=4, verbose_name='Cantidad' )
