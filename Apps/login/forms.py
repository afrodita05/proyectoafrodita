#Necesito modificar los forms asociados a la recuperación de contraseña.
#Tal vez hacer un override de los forms de reset de contraseña y llamar al OVERRIDE desde los html de reset de contraseña pueda servir


from django import forms
from django.contrib.auth.password_validation import MinimumLengthValidator
from Apps.login.models import *

from Apps.Usuarios.models import *

 #Se importan los validadores que aparecen al tratar de resetear la password. La intención es sobrecargar los métodos para cambiar la info que se muestra.
from django.core.exceptions import ValidationError
from django.utils.translation import ngettext

from django.forms import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime

from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm) #Más reciente intento

from django.utils.translation import gettext as _
 

import re

class UserPasswordResetForm(PasswordResetForm):
    
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo',
        'type': 'email',
        'name': 'email'
        }))


class UserSetPasswordForm(SetPasswordForm):
    
    error_messages = {
        'password_mismatch': _("Las contraseñas no coinciden."),
    }
    new_password1 = forms.CharField(label=_("Nueva contraseña"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("Repetir nueva contraseña"),
                                    widget=forms.PasswordInput)

    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user