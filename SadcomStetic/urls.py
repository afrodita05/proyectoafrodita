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
from Citas.views import Citas
from SadcomStetic import views
from login.views import login, recuperar_contrasena
from Usuarios.views import Usuarios
from Clientes.views import Clientes, Detalle_Cliente, Historial_Corporal, Historial_Facial
from Servicios.views import Servicios
from Proveedores.views import Proveedores
from Configuracion.views import Configuracion
from Compras.views import Compras, Crear_Compra

app_name = "SadcomStetic"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("settings", views.Settings.as_view(), name="settings"),
    path(
        "Login",
        view= login,
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
]
