from tkinter import Widget
from django.db import models
from django import forms

# Create your models here.



# Crear clase con el nombre de la tabla. Tener parámetros: models.Model
# Esto representa las tablas con sus atributos, donde models.tipodeatributo

class Usuarios(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    documento=models.CharField(max_length=10)
    nPersona= models.CharField(max_length=40,null=True)
    nUsuario= models.CharField(max_length=20)
    contrasena= models.CharField(max_length=20)
    correo= models.EmailField(blank=False,null=True)
    fechaCreacion= models.DateTimeField(auto_now=True) 
