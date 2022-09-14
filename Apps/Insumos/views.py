from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.


class Insumoview(TemplateView):
    pass

Insumos = Insumoview.as_view(
    template_name="pages/Insumos.html"
)
Crear_Insumo = Insumoview.as_view(
    template_name="pages/Crear-Insumo.html"
)