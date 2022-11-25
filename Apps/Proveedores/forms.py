from django import forms
from Apps.Proveedores.models import *
from django.forms import ValidationError
from dateutil.relativedelta import relativedelta
import re


class FormularioProveedor(forms.ModelForm):

    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        validarProveedor=re.search(r'^[a-zA-Z\s]{3,60}$',nombre, flags=re.MULTILINE)
        if validarProveedor==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres alfabéticos")
        return nombre 

    def clean_telefono(self):
        telefono=self.cleaned_data['telefono']
        validarTelefono=re.search(r'^[0-9]{7,10}$',telefono, flags=re.MULTILINE)
        if validarTelefono==None:
            raise ValidationError("Error. El número telefónico solo permite caracteres numéricos, entre 7 y 10 caracteres")
        return telefono

    def clean_direccion(self):
        direccion=self.cleaned_data['direccion']
        validarDireccion=re.search(r'^[a-zA-Z0-9\s#-]{2,50}$',direccion, flags=re.MULTILINE)
        if validarDireccion==None:
            raise ValidationError("Error. Solo se permite caracteres alfanuméricos, '#' o '-', entre 1 y 50 caracteres")
        return direccion

    def clean_correo(self):
        correo=self.cleaned_data['correo']
        validarDireccion=re.search(r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$',correo, flags=re.MULTILINE)
        if validarDireccion==None:
            raise ValidationError("Error. Solo se permite correos validos ")
        return correo


                          #select de un input
    
    

    class Meta:
        model=Proveedor
        fields='__all__'
        Choises=(                    #select de un input
            ('0', 'Activo'),
            ('1','Inactivo'),

            ) 

            
        #atributos de la tabla clientes
        
        widgets={      #los widgets son los campos de nuestra formulario donde  podremos asignar los atributos de nuestro formulario html
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre completo'}), 
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el número de teléfono'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la dirección'}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el correo electrónico'}),
            'proveedor':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la empresa'}),  
            'estado':forms.Select(choices=Choises,attrs={'class':'form-select'}),         
        }