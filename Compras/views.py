from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

User = get_user_model()
# class PagesView(LoginRequiredMixin, TemplateView):
class Compraview(TemplateView):
    pass

Compras = Compraview.as_view(
    template_name="pages/Compras.html"
)
Crear_Compra = Compraview.as_view(
    template_name="pages/Crear-Compra.html"
)