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

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = UserPasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(), #Convierte el literal byte a un string
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = UserPasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})