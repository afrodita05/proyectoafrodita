from django.db import models

# Create your models here.



# Crear clase con el nombre de la tabla. Tener parámetros: models.Model
# Esto representa las tablas con sus atributos, donde models.tipodeatributo

#class Usuarios(models.Model):
#    idUsuario=models.Autofield(primary_key=True)
 #   documento=models.
  #  nUsuario= models.#completar
   # contrasena= models.
    #correo= models.
    #fechaCreacion= models. 
    #estado= models. 
    #idRol= models.

class Prueba(models.Model):
    idPrueba=models.AutoField(primary_key=True)
    at1=models.CharField(max_length=11)
    at2=models.CharField(max_length=11)
    at3=models.CharField(max_length=11)

    #Makemigrations, y luego migrate