from django import forms
from Apps.Servicios.models import *
from django.forms import ValidationError
from datetime import datetime
import re


class FormularioServicio(forms.ModelForm):

    def clean_nServicio (self):
        nServicio=self.cleaned_data['nServicio']
        existe=Servicios.objects.filter(nServicio=nServicio).exists()
        validarNombre=re.search(r'^[a-zA-Z\s]{4,50}$',nServicio, flags=re.MULTILINE)
        print(existe)
        print(validarNombre, "VALIDAR")
        print("NOMBRE ES ", nServicio)
        
        return nServicio
        

    class Meta:
        model=Servicios
        fields='__all__' 
        widgets={      #los widgets son los campos de nuestra formulario donde  podremos asignar los atributos de nuestro formulario html
            'nServicio':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del servicio.'}),   
        }