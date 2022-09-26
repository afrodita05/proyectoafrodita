from django.db import models

# Create your models here.
class Rol(models.Model):
    idRol=models.AutoField(primary_key=True)
    nombreRol=models.CharField(max_length=60)
    permisoRol=models.CharField(max_length=25)


class RolesPermisos(models.Model):
    idRolesPermisos=models.AutoField(primary_key=True)
    idRol=models.ForeignKey(Rol, related_name='RolesPermisos', on_delete=models.PROTECT)

   

class permisoRol(models.Model):
    permisoConfiguracion="Configuracion"
    permisoInsumos="Insumos"
    permisoCitas="Citas"
    permisoCLientes="Clientes"
    permisoServicios="Servicios"
    permisoCompras="Compras"
    permisoProveedores="Proveedores"
    permisoUsuarios="Usuarios"

