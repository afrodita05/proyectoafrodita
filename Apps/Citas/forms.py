from datetime import datetime
from django import forms
from Apps.Citas.models import *
from django.forms import ValidationError
import re

class FormularioCitas(forms.ModelForm):
    def clean_fechaCita(self):
        fechaCita=self.cleaned_data['fechaCita']
        actual=datetime.now()
        actualStr=actual.strftime('%Y-%m-%d')
        if fechaCita<actualStr:
            raise  ValidationError("Error. se esta eligiendo una fecha de dias anteriores")
        return fechaCita

    class Meta:
        model=Citas
        fields='__all__'
        estadoCita=(
            ('Espera','Espera'),
            ('Proceso','Proceso'),
            ('Cancelado','Cancelado'),
            ('Finalizado','Finalizado'),
            )
        widgets={   
            'fechaCita':forms.TextInput(attrs={'class':'form-control','required data-pristine-required-message':'Por favor ingresa la fecha','type':'date'}),
            'estado':forms.Select(choices=estadoCita,attrs={'class':'form-select'}),
            'idServicio':forms.Select(attrs={'class':'form-select'}),
            'idCliente':forms.TextInput(attrs={'hidden':''}),
        }

class FormularioAgendaCosto(forms.ModelForm):
    # def clean_sesiones(self):
    #     sesiones=self.cleaned_data['sesiones']
    #     validarSesiones=re.search(r'^[0-9]{1,2}$',sesiones, flags=re.MULTILINE)
    #     if validarSesiones==None:
    #         raise ValidationError("Error. Solo se permite ingresar caracteres alfanuméricos ente 1 y 3 caracteres")
    #     return sesiones 
    # def clean_costo(self):
    #     costo=self.cleaned_data['costo']
    #     validarCosto=re.search(r'^[0-9]{1,8}$',costo, flags=re.MULTILINE)
    #     if validarCosto==None:
    #         raise ValidationError("Error. Solo se permite ingresar caracteres alfanuméricos ente 1 y 8 caracteres")
    #     return costo
    # def clean_abono(self):
    #     abono=self.cleaned_data['abono']
    #     validarAbono=re.search(r'^[0-9]{1,8}$',abono, flags=re.MULTILINE)
    #     if validarAbono==None:
    #         raise ValidationError("Error. Solo se permite ingresar caracteres alfanuméricos ente 1 y 8 caracteres")
    #     return abono

    class Meta:
        model=AgendaCosto
        fields='__all__'
        widgets={   
            'sesiones':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el Número de sesiones'}),
            'costo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el costo del servicio'}),
            'abono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el abono del servicio'}),
            'idCliente':forms.TextInput(attrs={'hidden':''}),
        }

class FormularioAgendaFecha(forms.ModelForm):
    class Meta:
        model=AgendaFecha
        fields='__all__'
        widgets={   
            'fechaAgenda':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'idAgendaCosto':forms.TextInput(attrs={'hidden':''}),
            'estado':forms.TextInput(attrs={'hidden':''}),
        }