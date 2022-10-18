from tkinter import Widget
from django import forms
from Apps.Clientes.models import *
from django.forms import ValidationError
import re

class FormularioCliente(forms.ModelForm):

    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        validarCliente=re.search(r'^[a-zA-Z\s]{2,60}$',nombre, flags=re.MULTILINE)
        if validarCliente==None:
            raise ValidationError("ERROR. Solo se permite ingresar caracteres alfabéticos")
        return nombre 
    
    def clean_documento(self):
        documento=self.cleaned_data['documento']
        existe=Clientes.objects.filter(documento=documento).exists()
        validarDocumento=re.search(r'^[0-9]{6,10}$',documento, flags=re.MULTILINE)
        if existe:
            raise ValidationError("Error.El documento ya existe")
        elif validarDocumento==None:
            raise ValidationError("Error. El documento solo permite caracteres numéricos, entre 6 y 10 caracteres")
        return documento
        
    def clean_telefono(self):
        telefono=self.cleaned_data['telefono']
        validarTelefono=re.search(r'^[0-9]{7,10}$',telefono, flags=re.MULTILINE)
        if validarTelefono==None:
            raise ValidationError("Error. El número telefónico solo permite caracteres numéricos, entre 7 y 10 caracteres")
        return telefono

    def clean_direccion(self):
        direccion=self.cleaned_data['direccion']
        validarDireccion=re.search(r'^[a-zA-Z0-9\s#-]{2,100}$',direccion, flags=re.MULTILINE)
        if validarDireccion==None:
            raise ValidationError("Error. Solo se permite caracteres alfanuméricos, # o -, entre 10 y 100 caracteres")
        return direccion
    
    def clean_numeroHijos(self):
        numeroHijos=self.cleaned_data['numeroHijos']
        validarNumeroHijos=re.search(r'^[0-9]{1,2}$',numeroHijos, flags=re.MULTILINE)
        if validarNumeroHijos==None:
            raise ValidationError("Error. El número de hijos solo permite caracteres numéricos, entre 1 y 2 caracteres")
        return numeroHijos

    class Meta:
        model=Clientes
        fields='__all__' #atributos de la tabla clientes
        sexoChoices=(                    #select de un input
            ('Masculino','Masculino'),
            ('Femenino','Femenino'),
            )
        estadoCivil=(
            ('Casado','Casado'),
            ('Union libre','Union libre'),
            ('Viudo','Viudo'),
            ('Soltero','Soltero'),
            )
        widgets={      #los widgets son los campos de nuestra formulario donde  podremos asignar los atributos de nuestro formulario html
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre completo'}),
            'documento':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el número de documento'}),
            'fechaNacimiento':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'sexo':forms.Select(choices=sexoChoices,attrs={'class':'form-select'}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el número de teléfono'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la dirección'}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el correo electrónico'}),
            'estadoCivil':forms.Select(choices=estadoCivil,attrs={'class':'form-select'}),
            'numeroHijos':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el número de hijos'})
            
        }


class FormularioCorporal(forms.ModelForm): 
    class Meta: 
        model=EsteticoCorporal
        fields='__all__'
        Choices=(                    #select de un input
            ('No','No'),
            ('Si','Si'),
            )
        siluetasChoices=(                    #select de un input
            ('Manzana','Manzana'),
            ('Rectangulo','Rectangulo'),
            ('Pera','Pera'),
            ('Reloj de arena','Reloj de arena'),
            ('Triangulo invertido','Triangulo invertido'),
            )
        modoVChoices=(                    #select de un input
            ('Activa','Activa'),
            ('Sedentaria','Sedentaria'),
            )
        calidadSChoices=(                    #select de un input
            ('Buena','Buena'),
            ('Mala','Mala'),
            )
        temperaturaChoices=(                    #select de un input
            ('Fría','Fría'),
            ('Tibia','Tibia'),
            ('Caliente','Caliente'),
            )
        widgets={
            'nombreE':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre completo','required':False}),
            #Sufre problemas
            'tensionA':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'digestivo':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'circulacion':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'endrocrino':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cardiacos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'otrosP':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            #Peso actual
            'kilos':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese kilos','required':False}),
            'talla':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese talla','required':False}),
            'altura':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese altura','required':False}),
            'masaC':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese masa corporal','required':False}),
            'siluetas':forms.Select(choices=siluetasChoices,attrs={'class':'form-select'}),
            'cirugias':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'fibrosis':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'costumbresA':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'deportesP':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            #Modo vida
            'modoV':forms.Select(choices=modoVChoices,attrs={'class':'form-select'}),
            'fuma':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'alcohol':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'calidadS':forms.Select(choices=calidadSChoices,attrs={'class':'form-select'}),
            'notasV':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            #Observaciones
            'problemasT':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            #Grasa localizada
            'abdomen':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'muslos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'nalgas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'espalda':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'piernas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'brazos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'notasO':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'tratamientosR':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'tratamientosE':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            #Antecedentes personales
            'dermatitis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cirugias1':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cualesC':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'hemofilia':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'embarazo':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cancer':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hepatitis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'diabetes':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'artritis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'artrosis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'escoliosis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'fracturas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'implantesM':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hipertencion':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'herniasD':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'dondeHD':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            'hiperlordosis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hipercifosis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'problemasC':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hipotension':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'osteoporosis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'osteomielitis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'comedones':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'pustulas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'brotes':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'quistes':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'nudulos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'zonasA':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
            #Adiposidadl
            'adiposidadL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'adiposidadZ':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'adiposidadC':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Cicatrices o estrías
            'cicatricesEL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cicatricesEZ':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cicatricesET':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Flacidez
            'flacidezL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'flacidezZ':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'flacidezC':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Alt.vasculares
            'altVascularesL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altVascularesZ':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altVascularesT':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Celulitis
            'celulitisL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'celulitisZ':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'celulitisC':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Temperatura
            'temperatura':forms.Select(choices=temperaturaChoices,attrs={'class':'form-select'}),
            #Alt.pigmentarias
            'altpigmentariasAR':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altpigmentariasAL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altpigmentariasAP':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altpigmentariasAMR':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altpigmentariasALV':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'altpigmentariasAPV':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Sensación
            'sensacionLG':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionMG':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionMUG':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionLF':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionMF':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionMUF':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionPD':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'sensacionPI':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'retieneL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'varices':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'arañitas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'observaciones':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
        
        }

   



