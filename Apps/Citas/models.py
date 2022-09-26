from django.db import models

# Create your models here.

class Clientes(models.Model):
    idCliente=models.AutoField(primary_key=True)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    nombre=models.CharField(max_length=60)
    sexo=models.CharField(max_length=9, blank=True,null=True)
    documento=models.CharField(max_length=10)
    fechaNacimiento=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10,blank=True,null=True )
    direccion=models.CharField(max_length=100,blank=True,null=True)
    correo=models.EmailField(blank=True,null=True)
    estadoCivil=models.CharField(max_length=11)
    numeroHijos=models.CharField(max_length=2)

class Citas(models.Model):
    idCitas=models.AutoField(primary_key=True)
    idCliente= models.ForeignKey(Clientes, related_name='Citas', on_delete=models.PROTECT)
    idServicio= models.ForeignKey('Servicios.Servicios', related_name='Citas', on_delete=models.PROTECT)
    fecha=models.CharField(max_length=10)   
    estado=models.CharField(max_length=50)

class estadosCitas():
    estadoEspera="espera"
    estadoProceso="proceso"
    estadoFinalizado="finalizado"
    estadoCancelado="cancelado"
