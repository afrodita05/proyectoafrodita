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
from Apps.Usuarios.views import Usuarios, Crear_Usuario, Editar_Usuario
from Apps.Clientes.views import cliente,formularioCliente,crearCliente,editarCliente,actualizarCliente, historialCorporal, historialFacial, detalleCliente, crearCorporal, crearFacial, crearMedidas
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
        "Clientes",
        view= cliente,
        name= "Clientes",
    ),
    path(
        "CrearCliente",
        view= crearCliente,
        name= "Clientes.Crear-Cliente",
    ),
    path(
        "EditarCliente",
        view= editarCliente,
        name= "Clientes.Editar-Cliente",
    ),
    path(
        "VerDetalle",
        view= detalleCliente,
        name= "Clientes.Ver-detalle",
    ),
    path(
        "CrearFacial",
        view= crearFacial,
        name= "Clientes.Ver-Detalles.Crear-Facial",
    ),
    path(
        "CrearCorporal",
        view= crearCorporal,
        name= "Clientes.Ver-Detalles.Crear-Corporal",
    ),
    path(
        "CrearMedias",
        view= crearMedidas,
        name= "Clientes.Ver-Detalles.Ver-Detalles-Corporal.Crear-Medida",
    ),
    path(
        "HistorialCoporal",
        view= historialCorporal,
        name= "Clientes.Ver-detalle.Historial-Corporal",
    ),
    path(
        "HistorialFacial",
        view= historialFacial,
        name= "Clientes.Ver-detalle.Historial-Facial",
    ),
    #path('listaClientes/',formularioClientes.as_view(),name='formularioFacial'),
   
    # path(
    #     "VerDetalle",
    #     view= Detalle_Cliente,
    #     name= "Clientes.Ver-detalle",
    # ),
    # path(
    #     "HistorialCoporal",
    #     view= Historial_Corporal,
    #     name= "Clientes.Ver-detalle.Historial-Corporal",
    # ),
    # path(
    #     "HistorialFacial",
    #     view= Historial_Facial,
    #     name= "Clientes.Ver-detalle.Historial-Facial",
    # ),
    '''
    path(
        "editarCliente/<int:id>",
        view=editarCliente,
        name= "editarCliente",
    ),
    path(
        "actualizarCliente/<int:id>",
        view=actualizarCliente,
        name= "actualizarCliente",
    ),
     
    path('listaClientes/',formularioClientes.as_view(),name='formularioFacial'),
    '''
   #CLIENTES
    
    # path(
    #     "VerDetalle",
    #     view= Detalle_Cliente,
    #     name= "Clientes.Ver-detalle",
    # ),
    # path(
    #     "HistorialCoporal",
    #     view= Historial_Corporal,
    #     name= "Clientes.Ver-detalle.Historial-Corporal",
    # ),
    # path(
    #     "HistorialFacial",
    #     view= Historial_Facial,
    #     name= "Clientes.Ver-detalle.Historial-Facial",
    # ),
]