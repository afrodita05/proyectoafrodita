from django.shortcuts import render, redirect


from django.contrib.auth import get_user_model

from Apps.Usuarios.models import * #importa usuarios


from django.urls import reverse
from django.views.generic import TemplateView

from Apps.login.forms import * #Importa forms de login

from django.db.models.query_utils import Q #Función Q de los querysets

from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError



# Create your views here.
class Loginview(TemplateView):
    pass


Login= Loginview.as_view(
    template_name="registration/login.html",
)

recuperar_contrasena= Loginview.as_view(
    template_name="pages/authentication/auth-recuperarContraseña.html",
)
