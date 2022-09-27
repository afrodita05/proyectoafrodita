from django.db import models
from Apps.Clientes.models import Clientes

# Create your models here.

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
