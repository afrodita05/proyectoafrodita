from tkinter import Widget
from django.db import models
from django import forms

# Create your models here.



# Crear clase con el nombre de la tabla. Tener parámetros: models.Model
# Esto representa las tablas con sus atributos, donde models.tipodeatributo

class Usuarios(models.Model):
    idUsuario=models.Autofield(primary_key=True)
    documento=models.CharField(max_length=10)
    nUsuario= models.CharField(max_length=20)
    contrasena= models.CharField(max_length=20, Widget=forms.PasswordInput)
    correo= models.EmailField(blank=False,null=False)
    fechaCreacion= models.DateTimeField(auto_now=True) 
    #estado= models. 
    #idRol= models.

    #Makemigrations, y luego migrate
