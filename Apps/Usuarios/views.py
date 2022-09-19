from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.
class Usuarioview(TemplateView):
    pass

Usuarios = Usuarioview.as_view(
    template_name="Usuarios/Usuarios.html"
)
def formularioUsuarios(request):
    return render(request,"Usuarios/Usuarios.html",Usuarios)

Crear_Usuario = Usuarioview.as_view(
    template_name="Usuarios/Crear-Usuario.html"
)
Editar_Usuario = Usuarioview.as_view(
    template_name="Usuarios/Editar-Usuario.html"
)