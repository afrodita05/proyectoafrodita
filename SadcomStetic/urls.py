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
from django.contrib.auth import views as auth_views
from Apps.login.forms import UserPasswordResetForm, UserSetPasswordForm #aa

from SadcomStetic import views

from Apps.Citas.views import *
from Apps.login.views import Login, recuperar_contrasena
# from Apps.Usuarios.views import Usuarios, Crear_Usuario, Editar_Usuario
from Apps.Clientes.views import *
from Apps.Usuarios.views import *
from Apps.Servicios.views import *
from Apps.Configuracion.views import *
from Apps.Proveedores.views import CrearProveedor,ListarProveedor,EditarProveedor
from Apps.Compras.views import FormularioAgregarCompra,CrearCompra,ListarCompra,DetalleCompras, FormularioAgregarInsumo, CrearInsumo, estadoCompra, estadocompra 
from Apps.Insumos.views import insumos


app_name = "SadcomStetic"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.DashboardView.as_view(), name="dashboard"),
    
    path('login/', 
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ), 
        name="login"
    ),

    path('logout', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),


    path('accounts/', include('django.contrib.auth.urls')),

    path('reset_password', auth_views.PasswordResetView.as_view(form_class=UserPasswordResetForm), name='password_reset',), 
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(form_class=UserSetPasswordForm), name='password_reset_confirm'), #Funcional. Buscar en la documentación de django el form_class para modificarlo por un extend (override) del original
   


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
    path('actualizarU/<int:id>',actualizarU, name='actualizarU'),



    #SERVICIOS
    path(
    "servicio",
        view= servicio,
        name= "Servicio",
    ),
    path('crearServicio/',crearServicio),
    path('rutaV/',rutaV),
    path('verificacionServicio/',verificacionServicio),
    path('verificacionServicioEditar/<int:id>',verificacionServicioEditar, name='verificacionServicioEditar'),
    path('formularioServicio/<int:id>',formularioServicio, name='formularioServicio'),
    path('editarS/<int:id>',editarS, name='editarServicio'),
    path('actualizarS/<int:id>',actualizarS, name='actualizarServicio'),
    path('eliminarS/<int:id>',eliminarS, name='eliminarServicio'),

    #PROVEEDORES
  
    path(
        "ListarProveedor/", 
         view=ListarProveedor,
         name= "Proveedor"
        ),
         
    path(
        'CrearProveedor/',
         CrearProveedor
        ),

    path(
        'EditarProveedor/<int:id>',
        EditarProveedor, 
        name='EditarProveedor'
        ),
    # path('FormularioAgregarProveedor/', FormularioAgregarProveedor),
    #path('ActualizarProveedor/<int:idProveedor>',ActualizarProveedor, name='ActualizarProveedor'),

    #CONFIGURACION

    path(
        'crearRol/',
        view=crearRol, 
        name= 'crearRol'
        ),
    path(
        'formularioRol/',
        view=formularioRol, 
        name='formularioRol'
        ),
    path(
        'listarRol/',
        view=listarRol, 
        name='Rol'
        ),
    
    path(
        'detalleRol/<int:id>',
        view=detalleRol, 
        name='detalleRol'
        ),

    path(
        'editarRol/<int:id>',
        view=editarRol, 
        name='editarRol'
        ),

    path(
        'actualizarRol/<int:id>',
        view=actualizarRol, 
        name='actualizarRol'
        ),
    # path(
    #     'editarRol/<int:id>',
    #     view=editarRol, 
    #     name='editarRol'),


    # path('actualizarRol/<int:id>',actualizarRol, name='actualizarRol'),
    
 
    #CITAS
    path(
        'Cita/',
        view=listarCita, 
        name='Cita'
        ),

     path(
        'verficarDocumento/',
        view=verificarDocumento, 
        name='verificar-Documento'
        ),   

    path(
        'crearCitas/<int:id>',
        view=crearCita, 
        name='crear-Citas'
        ),

    path(
        'editarCitas/<int:id>',
        view=editarCita, 
        name='editar-Citas'
        ),   

    path(
        'verDetalleCita/<int:id>',
        view=verDetalleCita, 
        name='verDetalle-Cita'
        ),

    path(
        'crearCosto/<int:id>',
        view=crearAgendaCosto, 
        name='Agenda-Costo'
        ),

     path(
        'editarCosto/<int:id>',
        view=editarAgendaCosto, 
        name='Editar-Costo'
        ),    

    path(
        'verDetalleCosto/<int:id>',
        view=verDetalleCosto, 
        name='verDetalle-Costo'
        ),

    path(
        'crearFecha/<int:id>',
        view=crearAgendaFecha, 
        name='Agenda-Fecha'
        ),

     path(
        'editarFecha/<int:id>',
        view=editarFechaAgenda, 
        name='Editar-Fecha'
        ),
    
    
    #COMPRAS
    path( "ListarCompra/", view= ListarCompra,name= "Compra"),
    path('CrearCompra/', CrearCompra, name='CrearCompra'),
    path('CrearInsumo/', CrearInsumo, name='CrearInsumo'),
    path('FormularioAgregarInsumo/', FormularioAgregarInsumo,),
    path('FormularioAgregarCompra/', FormularioAgregarCompra,),
    path('DetalleCompras/<int:id>', DetalleCompras, name='DetalleCompras'),
    path('EstadoCompra/<int:id>', estadoCompra, name='estadocompra'),
    path('actualizarE/<int:id>', estadocompra, name= 'actualizarE'),
    
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
        view= listarCliente,
        name= "Clientes",
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
        "VerDetalle/<int:id>",
        view= detalleCliente,
        name= "Clientes.Ver-detalle",
    ),

    path(
        "CrearCorporal/<int:id>",
        view= crearCorporal,
        name= "Crear-Corporal",
    ),
    
    path(
        "VerDetalleCorporal/<int:id>",
        view= VerDetalleCorporal,
        name= "Clientes.Ver-Detalles.Corporal",
    ),

    path(
        "CrearFacial/<int:id>",
        view= crearFacial,
        name= "Crear-Facial",
    ),

    path(
        "VerDetalleFacial/<int:id>",
        view= VerDetalleFacial,
        name= "Clientes.Ver-Detalles.Facial",
    ),

    path(
        "CrearControlMedidas/<int:id>",
        view= crearControlMedidas,
        name= "Clientes.Ver-Detalles.Crear-Control-Medidas",
    ),
    
]