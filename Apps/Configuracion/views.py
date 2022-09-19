from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

class Configuracionview(TemplateView):
    pass

Configuracion = Configuracionview.as_view(
    template_name="Configuracion/Configuracion.html"
)
Crear_rol = Configuracionview.as_view(
    template_name="Configuracion/Crear-Rol.html"
)
Permisos = Configuracionview.as_view(
    template_name="Configuracion/Permisos.html"
)
