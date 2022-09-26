from django.db import models

# Create your models here.

class Proveedor(models.Model):
    idProveedor=models.AutoField(primary_key=True)
    proveedor=models.CharField(max_length=30)
    producto=models.CharField(max_length=30)
    telefono=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    correo=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)