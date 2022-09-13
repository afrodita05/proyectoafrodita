from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

User = get_user_model()
# class PagesView(LoginRequiredMixin, TemplateView):
class Clienteview(TemplateView):
    pass


Clientes = Clienteview.as_view(
    template_name="pages/Clientes.html"
)
Detalle_Cliente = Clienteview.as_view(
    template_name="pages/Detalles-Clientes.html"
)
Historial_Corporal = Clienteview.as_view(
    template_name="pages/Historial-Corporal.html"
)
Historial_Facial = Clienteview.as_view(
    template_name="pages/Historial-Facial.html"
)