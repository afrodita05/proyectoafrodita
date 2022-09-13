from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.
class Loginview(TemplateView):
    pass

Login= Loginview.as_view(
    template_name="pages/authentication/auth-login.html",
)

recuperar_contrasena= Loginview.as_view(
    template_name="pages/authentication/auth-recuperarContraseña.html",
)