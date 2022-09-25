from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.
class Servicioview(TemplateView):
    pass

Servicios= Servicioview.as_view(
    template_name="Servicios/Servicios.html",
)
Crear_Servicio= Servicioview.as_view(
    template_name="Servicios/Crear-Servicio.html",
)
Editar_Servicio= Servicioview.as_view(
    template_name="Servicios/Editar-Servicio.html",
)
Detalle_Servicio= Servicioview.as_view(
    template_name="Servicios/Ver-Detalle.html",
)

