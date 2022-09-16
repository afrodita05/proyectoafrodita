from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

# Se pueden hacer en clases o funciones
# 

class Usuarioview(TemplateView):
    pass

Usuarios = Usuarioview.as_view(
    template_name="pages/Usuarios.html"
)