from django.db import models

# Create your models here.

class Servicios(models.Model):
    idServicio=models.AutoField(primary_key=True)
    nServicio=models.CharField(max_length=50)
    tiempo= models.IntegerField()
