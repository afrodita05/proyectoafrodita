from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

class Compraview(TemplateView):
    pass

Compras = Compraview.as_view(
    template_name="Compras/Compras.html"
)
Crear_Compra = Compraview.as_view(
    template_name="Compras/Crear-Compra.html"
)
Detalle_Compra = Compraview.as_view(
    template_name="Compras/Ver-Detalle.html"
)