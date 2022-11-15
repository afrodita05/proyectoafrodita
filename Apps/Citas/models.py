from django.db import models
from Apps.Clientes.models import Clientes
from Apps.Servicios.models import Servicios


# Create your models here.

class Citas(models.Model):
    idCita=models.AutoField(primary_key=True)
    idCliente=models.ForeignKey(Clientes, on_delete=models.PROTECT)
    fechaCita=models.CharField(max_length=60)
    estado=models.CharField(max_length=10)
    idServicio=models.ForeignKey(Servicios,on_delete=models.PROTECT)

class AgendaCosto(models.Model):
    idAgendaCosto=models.AutoField(primary_key=True)
    idCliente=models.ForeignKey( Clientes, on_delete=models.PROTECT)
    sesiones=models.CharField(max_length=2)
    costo=models.IntegerField()
    abono=models.IntegerField()
    
class AgendaFecha(models.Model):
    idAgendaFecha=models.AutoField(primary_key=True)
    idAgendaCosto=models.ForeignKey(AgendaCosto, on_delete=models.PROTECT)
    fechaAgenda=models.CharField(max_length=10)
    estado=models.CharField(max_length=9)
