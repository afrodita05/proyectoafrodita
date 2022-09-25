from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

class Citaview(TemplateView):
    pass

Citas = Citaview.as_view(
    template_name="Citas/Citas.html"
)
Crear_Cita = Citaview.as_view(
    template_name="Citas/Crear-Cita.html"
)
Editar_Cita = Citaview.as_view(
    template_name="Citas/Editar-Cita.html"
)