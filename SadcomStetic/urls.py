"""SadcomStetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cmath import log
from http import client
from django.contrib import admin
from django.urls import path
from SadcomStetic import views

from Apps.Citas.views import Citas, Editar_Cita, Crear_Cita
from Apps.login.views import Login, recuperar_contrasena
from Apps.login.views import Login, recuperar_contrasena
# from Apps.Usuarios.views import Usuarios, Crear_Usuario, Editar_Usuario
from Apps.Clientes.views import cliente,formularioCliente,crearCliente,editarCliente,actualizarCliente,detalleCliente,formularioCorporal,crearCorporal,VerDetalleCorporal,formularioFacial,crearFacial,VerDetalleFacial,formularioControlMedidas,crearControlMedidas,formularioPagosSesionesCorporal,crearPagosSesionesCorporal,formularioPagosSesionesFacial,crearPagosSesionesFacial
from Apps.Servicios.views import Servicios, Crear_Servicio, Editar_Servicio, Detalle_Servicio
from Apps.Proveedores.views import Proveedores, Crear_Proveedor, Editar_Proveedor
from Apps.Configuracion.views import Configuracion, Crear_rol, Permisos
from Apps.Compras.views import Compras, Crear_Compra, Detalle_Compra
from Apps.Insumos.views import Insumos, Crear_Insumo

app_name = "SadcomStetic"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.DashboardView.as_view(), name="dashboard"),
    path(
        "Login",
        view= Login,
        name= "pages.authentication.login",
    ),
    path(
        "Recuperar contraseña",
        view= recuperar_contrasena,
        name= "pages.authentication.recuperarContraseña",
    ),
#urls acorta las rutas para buscar path
#Siempre que vaya a crear una vista debo asignarle una URL

    #SERVICIOS
    path(
        "Servicios",
        view= Servicios,
        name= "Servicios",
    ),
    path(
        "CrearServicio",
        view= Crear_Servicio,
        name= "Servicios.Crear_Servicio",
    ),
    path(
        "EditarServicio",
        view= Editar_Servicio,
        name= "Servicios.Editar-Servicio",
    ),
    path(
        "DetalleServicios",
        view= Detalle_Servicio,
        name= "Servicios.Ver-Detalle",
    ),
    #PROVEEDORES
    path(
        "Proveedores",
        view= Proveedores,
        name= "Proveedores",
    ),
    path(
        "CrearProveedor",
        view= Crear_Proveedor,
        name= "Proveedores.Crear-Proveedor",
    ),
    path(
        "EditarProveedor",
        view= Editar_Proveedor,
        name= "Proveedores.Editar-Proveedor",
    ),
    path(
        "Configuracion",
        view= Configuracion,
        name= "Configuracion",
    ),
    #CONFIGURACION
    path(
        "Configuracion",
        view= Configuracion,
        name= "Configuracion",
    ),
    path(
        "CrearRol",
        view= Crear_rol,
        name= "Configuracion.Crear-Rol",
    ),
    path(
        "Permisos",
        view= Permisos,
        name= "Configuracion.Permisos",
    ),
    #CITAS
    path(
        "Citas",
        view= Citas,
        name= "Citas",
    ),
    path(
        "CrearCita",
        view= Crear_Cita,
        name= "Citas.Crear-Cita",
    ),
    path(
        "EditarCita",
        view= Editar_Cita,
        name= "Citas.Editar-Cita",
    ),
    #COMPRAS
    path(
        "Compras",
        view= Compras,
        name= "Compras",
    ),
    path(
        "CrearCompra",
        view= Crear_Compra,
        name= "Compras.Crear-Compras",
    ),
    path(
        "DetalleCompra",
        view= Detalle_Compra,
        name= "Compras.Detalles-De-Compra",
    ),
    #INSUMOS
    path(
        "Insumos",
        view= Insumos,
        name= "Insumos",
    ),
    path(
        "CrearInsumo",
        view= Crear_Insumo,
        name= "Insumos.Crear-Insumo",
    ),
    #CLIENTES
    path(
        "Clientes/", 
        view= cliente,
        name= "Clientes",
    ),

    path(
        "FormularioCliente/",
        view= formularioCliente,
        name= "Clientes.Formulario-Cliente",
    ),

    path(
        "CrearCliente/",
        view= crearCliente,
        name= "Clientes.Crear-Cliente",
    ),

    path(
        "EditarCliente/<int:id>",
        view= editarCliente,
        name= "Clientes.Editar-Cliente",
    ),

     path(
        "ActualizarCliente/<int:id>",
        view= actualizarCliente,
        name= "Clientes.Actualizar-Cliente",
    ),

    path(
        "VerDetalle/<int:id>",
        view= detalleCliente,
        name= "Clientes.Ver-detalle",
    ),

    path(
        "FormularioCorporal/<int:id>",
        view= formularioCorporal,
        name= "Clientes.Formulario-Corporal",
    ),

    path(
        "CrearCorporal/<int:id>",
        view= crearCorporal,
        name= "Clientes.Ver-Detalles.Crear-Corporal",
    ),
    
    path(
        "VerDetalleCorporal/<int:id>",
        view= VerDetalleCorporal,
        name= "Clientes.Ver-Detalles.Corporal",
    ),

    path(
        "FormularioFacial/<int:id>",
        view= formularioFacial,
        name= "Clientes.Formulario-Facial",
    ),

    path(
        "CrearFacial/<int:id>",
        view= crearFacial,
        name= "Clientes.Ver-Detalles.Crear-Facial",
    ),

    path(
        "VerDetalleFacial/<int:id>",
        view= VerDetalleFacial,
        name= "Clientes.Ver-Detalles.Facial",
    ),

    path(
        "FormularioControlMedidas/<int:id>",
        view= formularioControlMedidas,
        name= "Clientes.Ver-Detalles.Formulario-Control-Medidas",
    ),

    path(
        "CrearControlMedidas/<int:id>",
        view= crearControlMedidas,
        name= "Clientes.Ver-Detalles.Crear-Control-Medidas",
    ),
    path(
        "FormularioPagoSesionCorporal/<int:id>",
        view= formularioPagosSesionesCorporal,
        name= "Clientes.Ver-Detalles.Formulario-Pagos-Sesiones-Corporal",
    ),
       path(
        "CrearPagoSesionCorporal/<int:id>",
        view= crearPagosSesionesCorporal,
        name= "Clientes.Ver-Detalles.Crear-Pagos-Sesiones-Corporal",
    ),
     path(
        "FormularioPagoSesionFacial/<int:id>",
        view= formularioPagosSesionesFacial,
        name= "Clientes.Ver-Detalles.Formulario-Pagos-Sesiones-Facial",
    ),
       path(
        "CrearPagoSesionFacial/<int:id>",
        view= crearPagosSesionesFacial,
        name= "Clientes.Ver-Detalles.Crear-Pagos-Sesiones-Facial",
    ),

    
    #slash al final del ruta  
 
]