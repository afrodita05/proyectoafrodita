from django.db import models

# Create your models here.

class Proveedor(models.Model):
    idProveedor=models.AutoField(primary_key=True)
    proveedor=models.CharField(max_length=60)
    telefono=models.CharField(max_length=10)
    nombre=models.CharField(max_length=60)
    correo=models.CharField(max_length=40)
    direccion=models.CharField(max_length=50)
    estado=models.BooleanField(default=True, verbose_name="estado")