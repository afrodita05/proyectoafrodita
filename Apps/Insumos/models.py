
from django.db import models
# Create your models here.

class Insumo(models.Model):
    idInsumo= models.AutoField(primary_key=True) 
    nombre = models.TextField(null= True, verbose_name='Nombre')
    cantidad = models.CharField(null= True, max_length=4, verbose_name='Cantidad' )
    def __str__(self):
        fila ="Insumo: " + self.insumo + " - " + "Canidad: " +self.cantidad 
        return fila