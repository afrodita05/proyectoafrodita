from django.db import models

# Create your models here.

class Proveedor(models.Model):
    idProveedor=models.AutoField(primary_key=True)
    proveedor=models.CharField(max_length=20)
    producto=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10)
    nombre=models.CharField(max_length=10)
    correo=models.CharField(max_length=10)
    direccion=models.CharField(max_length=10)