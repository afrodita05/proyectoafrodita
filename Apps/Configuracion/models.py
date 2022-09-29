from django.db import models

# Create your models here.
class Rol(models.Model):
    idRol=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60)
    configuracion=models.CharField(max_length=60,blank=True,null=True)
    insumos=models.CharField(max_length=60,blank=True,null=True)
    citas=models.CharField(max_length=60,blank=True,null=True)
    clientes=models.CharField(max_length=60,blank=True,null=True)
    servicios=models.CharField(max_length=60,blank=True,null=True)
    compras=models.CharField(max_length=60,blank=True,null=True)
    proveedores=models.CharField(max_length=60,blank=True,null=True)
    usuarios=models.CharField(max_length=60,blank=True,null=True)


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
