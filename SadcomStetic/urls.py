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
from Apps.Citas.views import Citas
from SadcomStetic import views
from Apps.login.views import Login, recuperar_contrasena
from Apps.Usuarios.views import Usuarios
from Apps.Clientes.views import Clientes, Detalle_Cliente, Historial_Corporal, Historial_Facial
from Apps.Servicios.views import Servicios
from Apps.Proveedores.views import Proveedores
from Apps.Configuracion.views import Configuracion
from Apps.Compras.views import Compras, Crear_Compra
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
    path(
        "Clientes",
        view= Clientes,
        name= "Clientes",
    ),
    path(
        "Usuarios",
        view=  Usuarios,
        name= "Usuarios",
    ),
    path(
        "Servicios",
        view= Servicios,
        name= "Servicios",
    ),
    path(
        "Proveedores",
        view= Proveedores,
        name= "Proveedores",
    ),
    path(
        "Configuracion",
        view= Configuracion,
        name= "Configuracion",
    ),
    path(
        "Citas",
        view= Citas,
        name= "Citas",
    ),
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
        "VerDetalle",
        view= Detalle_Cliente,
        name= "Clientes.Ver-detalle",
    ),
    path(
        "HistorialCoporal",
        view= Historial_Corporal,
        name= "Clientes.Ver-detalle.Historial-Corporal",
    ),
    path(
        "HistorialFacial",
        view= Historial_Facial,
        name= "Clientes.Ver-detalle.Historial-Facial",
    ),
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
]
