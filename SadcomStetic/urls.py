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
from django.urls import path, include
from SadcomStetic import views

from Apps.Citas.views import crearCita, formularioCita, listarCita, editarCita, editarCliente, actualizarCita, actualizarCliente,servicio
from Apps.login.views import Login, recuperar_contrasena
from Apps.login.views import Login, recuperar_contrasena
# from Apps.Usuarios.views import Usuarios, Crear_Usuario, Editar_Usuario
from Apps.Clientes.views import cliente,formularioCliente,crearCliente,detalleCliente,formularioCorporal,crearCorporal,VerDetalleCorporal,formularioFacial,crearFacial,VerDetalleFacial,formularioControlMedidas,crearControlMedidas,formularioPagosSesionesCorporal,crearPagosSesionesCorporal,formularioPagosSesionesFacial,crearPagosSesionesFacial
from Apps.Usuarios.views import usuario, crearUsuario, formularioUsuario, editarU, actualizarU
from Apps.Servicios.views import servicio, crearServicio, formularioServicio, editarS, actualizarS, eliminarS
from Apps.Proveedores.views import Proveedores, Crear_Proveedor, Editar_Proveedor
from Apps.Configuracion.views import crearRol,actualizarRol,formularioRol,editarRol,listarRol
from Apps.Compras.views import Compras, Crear_Compra, Detalle_Compra
from Apps.Insumos.views import insumos

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


    #USUARIOS

    path(
    "usuario",
        view= usuario,
        name= "Usuario",
    ),
    
    path('crearUsuario/',crearUsuario),
    path('formularioUsuario/',formularioUsuario),
    path('editarU/<int:id>',editarU, name='editarUsuario'),
    path('actualizarU/<int:id>',actualizarU, name='actualizarUsuario'),



    #SERVICIOS
    path(
    "servicio",
        view= servicio,
        name= "Servicio",
    ),
    path('crearServicio/',crearServicio),
    path('formularioServicio/',formularioServicio),
    path('editarS/<int:id>',editarS, name='editarServicio'),
    path('actualizarS/<int:id>',actualizarS, name='actualizarServicio'),
    path('eliminarS/<int:id>',eliminarS, name='eliminarServicio'),

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

    #CONFIGURACION

    path('crearRol/',crearRol, name= 'crearRol'),
    path('editarRol/<int:id>',editarRol, name='editarRol'),
    path('actualizarRol/<int:id>',actualizarRol, name='actualizarRol'),
    path('formularioRol/',formularioRol, name='formularioRol'),
    path('listarRol/',listarRol, name='Rol'),


    #CITAS
    path(
        "listarCita",
        view= listarCita,
        name= "Cita",
    ),
    path('crearCita/',crearCita,name='crearCita'),
    path('formularioCita/',formularioCita, name='formularioCita'),
    path('editarCita/<int:id>',editarCita, name='editarCita'),
    path('editarCliente/<int:id>',editarCliente, name='editarCliente'),
    path('actualizarCita/<int:id>',actualizarCita, name='actualizarCita'),
    path('actualizarCliente/<int:id>',actualizarCliente, name='actualizarCliente'),
    
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
        view= insumos,
        name= "Insumos",
    ),
    path ('', include ('Apps.Insumos.urls')),
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

]