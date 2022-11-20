from django.db import models
from Apps.Clientes.models import Clientes
from Apps.Servicios.models import Servicios


# Create your models here.

class Citas(models.Model):
    idCita=models.AutoField(primary_key=True)
    idCliente=models.ForeignKey(Clientes, null=True, on_delete=models.PROTECT)
    fechaCita=models.CharField(max_length=60)
    estado=models.CharField(max_length=10)
    idServicio=models.ForeignKey(Servicios,on_delete=models.PROTECT)

class AgendaCosto(models.Model):
    idAgendaCosto=models.AutoField(primary_key=True)
    idCita=models.ForeignKey( Citas, null=True, on_delete=models.PROTECT)
    sesiones=models.CharField(max_length=2)
    costo=models.CharField(max_length=8)
    abono=models.CharField(max_length=8)
    
class AgendaFecha(models.Model):
    idAgendaFecha=models.AutoField(primary_key=True)
    idAgendaCosto=models.ForeignKey(AgendaCosto, on_delete=models.PROTECT)
    fechaAgenda=models.CharField(max_length=10)
    estado=models.CharField(max_length=9)
