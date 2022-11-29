from django.db import models

# Create your models here.



# class Permiso(models.Model):
#     idPermisos=models.AutoField(primary_key=True)
#     idRol=models.ForeignKey(Rol, on_delete=models.PROTECT)
#     permisoConfiguracion=models.CharField(max_length=60)
#     permisoInsumos=models.CharField(max_length=60)
#     permisoCitas=models.CharField(max_length=60)
#     permisoCLientes=models.CharField(max_length=60)
#     permisoServicios=models.CharField(max_length=60)
#     permisoCompras=models.CharField(max_length=60)
#     permisoProveedores=models.CharField(max_length=60)
#     permisoUsuarios=models.CharField(max_length=60)


# class RolesPermisos(models.Model):
#     idRolesPermisos=models.AutoField(primary_key=True)
#     idRol=models.ForeignKey(Rol, related_name='RolesPermisos', on_delete=models.PROTECT)
