from django import forms
from Apps.Clientes.models import *
from django.forms import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime
import re


class FormularioCliente(forms.ModelForm):

    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        validarCliente=re.search(r'^[a-zA-Z\s]{3,60}$',nombre, flags=re.MULTILINE)
        if validarCliente==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres alfabéticos")
        return nombre 
    
    def clean_documento(self):
        documento=self.cleaned_data['documento']
        existe=Clientes.objects.filter(documento=documento).exists()
        validarDocumento=re.search(r'^[0-9]{6,10}$',documento, flags=re.MULTILINE)
        if existe:
            raise ValidationError("Error. El documento ya existe")
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
        validarDireccion=re.search(r'^[a-zA-Z0-9\s#-]{2,50}$',direccion, flags=re.MULTILINE)
        if validarDireccion==None:
            raise ValidationError("Error. Solo se permite caracteres alfanuméricos, '#' o '-', entre 10 y 100 caracteres")
        return direccion
    
    def clean_numeroHijos(self):
        numeroHijos=self.cleaned_data['numeroHijos']
        validarNumeroHijos=re.search(r'^[0-9]{1,2}$',numeroHijos, flags=re.MULTILINE)
        if validarNumeroHijos==None:
            raise ValidationError("Error. Solo se permite caracteres numéricos, entre 1 y 2 caracteres")
        return numeroHijos

    def clean_fechaNacimiento(self):  #para relativedelta hay que instalar "pip install python-dateutil"
        actual=datetime.now()
        actualStr=actual.strftime('%Y-%m-%d')
        mayorEdad=relativedelta(years=-17)
        sumaFecha=actual+mayorEdad
        sumaFechaStr=sumaFecha.strftime('%Y-%m-%d')
        fechaNacimento=self.cleaned_data['fechaNacimiento']
        if fechaNacimento==actualStr or fechaNacimento>sumaFechaStr:
             raise ValidationError("Error. El cliente es menor de edad")
        return fechaNacimento

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
    def clean_kilos(self):
        kilos=self.cleaned_data['kilos']
        validarKilos=re.search(r'^[0-9.]{1,7}$',kilos, flags=re.MULTILINE)
        if validarKilos==None:
            raise ValidationError("Error. Solo se permite ingresar decimales")
        return kilos 
    def clean_talla(self):
        talla=self.cleaned_data['talla']
        validarTalla=re.search(r'^[0-9.]{1,7}$',talla, flags=re.MULTILINE)
        if validarTalla==None:
            raise ValidationError("Error. Solo se permite ingresar decimales")
        return talla
    def clean_altura(self):
        altura=self.cleaned_data['altura']
        validarAltura=re.search(r'^[0-9.]{1,7}$',altura, flags=re.MULTILINE)
        if validarAltura==None:
            raise ValidationError("Error. Solo se permite ingresar decimales")
        return altura 
    def clean_masaC(self):
        masaC=self.cleaned_data['masaC']
        validarMasaC=re.search(r'^[0-9.]{1,7}$',masaC, flags=re.MULTILINE)
        if validarMasaC==None:
            raise ValidationError("Error. Solo se permite ingresar decimales")
        return masaC
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
            'aranitas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'observaciones':forms.Textarea(attrs={'class':'form-control','required':False,'id':'progresspill-address-input','rows':'2'}),
        
        }

class FormularioFacial(forms.ModelForm): 
    class Meta: 
        model=EsteticoFacial
        fields='__all__'
        Choices=(                   
            ('No','No'),
            ('Si','Si'),
            )
        siluetasChoices=(                    
            ('Manzana','Manzana'),
            ('Rectangulo','Rectangulo'),
            ('Pera','Pera'),
            ('Reloj de arena','Reloj de arena'),
            ('Triangulo invertido','Triangulo invertido'),
            )
        FototipoChoices=(                    
            ('Fototipo 1','Fototipo 1'),
            ('Fototipo 2','Fototipo 2'),
            ('Fototipo 3','Fototipo 3'),
            ('Fototipo 4','Fototipo 4'),
            ('Fototipo 5','Fototipo 5'),
            ('Fototipo 6','Fototipo 6'),
            )
        widgets={
            'nombreE':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre completo','required':False}),
            #Factores agravantes
            'tratamientoM':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cualTM':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'¿Cuál tratamiento Medico?','required':False}),
            'sustitucionH':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'tomaA':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'drogas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'alimentosP':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese los alimentos preferidos','required':False}),
            'alimentosR':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese los alimentos rechazados','required':False}),
            'fuma':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'tomaL':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'protegeS':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'duermeB':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'menopausia':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'medicamentosOT':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cualesOT':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese los medicamentos orales o tópicos','required':False}),
            'padeceE':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cancerP':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'asma':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'lupus':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'herpes':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hepatitis':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'epilepsias':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'dolorC':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'ampollasF':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'tiroides':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'problemasC':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'psicologicos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'urinarios':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'nasales':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'digestivos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Está utilizando o uso
            'alfahidroxiacidos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'retinA':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'differin':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'accutane':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'motivoC':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese el motivo de la consulta','required':False}),
            'productoCM':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese los productos a los que es alérgico','required':False}),
            #Analisis de piel
            'normal':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'gruesa':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'aspera':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'suave':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'normal1':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cerrado':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'dilatado':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Brillo
            'zonasM':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'zonasB':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Grado de hidratación
            'normal2':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'deshidratada':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hiperdeshidratada':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Fototipo de piel
            'fototipoP':forms.Select(choices=FototipoChoices,attrs={'class':'form-select'}),
            #Alteraciones del envejecimiento
            'lineasF':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'profundas':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'flacidez':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'parpados':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'cuello':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'nasogenianos':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'labios':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Acné(desde cuándo)
            'comedones':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'milias':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'quistes':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Pigmentación
            'melasma':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'hipercromia':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'edema':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'grasa':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            #Cuidados que realiza diariamente
            'rutinasH':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese las rutinas diarias de higiene','required':False}),
            'cuidadosH':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese los cuidados habituales','required':False}),
            'mensuales':forms.Select(choices=Choices,attrs={'class':'form-select'}),
            'productoH':forms.Textarea(attrs={'class':'form-control','id':'progresspill-address-input','rows':'2','placeholder':'Ingrese los productos que utiliza habitualmente','required':False}),
            
        }
        
class FormularioMedidas(forms.ModelForm): 
    def clean_brazoD(self):
        brazoD=self.cleaned_data['brazoD']
        validarbrazoD=re.search(r'^[0-9,]{1,7}$',brazoD, flags=re.MULTILINE)
        if validarbrazoD==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return brazoD
    def clean_brazoI(self):
        brazoI=self.cleaned_data['brazoI']
        validarbrazoI=re.search(r'^[0-9,]{1,7}$',brazoI, flags=re.MULTILINE)
        if validarbrazoI==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return brazoI
    def clean_abdomenA(self):
        abdomenA=self.cleaned_data['abdomenA']
        validarabdomenA=re.search(r'^[0-9,]{1,7}$',abdomenA, flags=re.MULTILINE)
        if validarabdomenA==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return abdomenA
    def clean_cintura(self):
        cintura=self.cleaned_data['cintura']
        validarcintura=re.search(r'^[0-9,]{1,7}$',cintura, flags=re.MULTILINE)
        if validarcintura==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return cintura
    def clean_abdomenB(self):
        abdomenB=self.cleaned_data['abdomenB']
        validarabdomenB=re.search(r'^[0-9,]{1,7}$',abdomenB, flags=re.MULTILINE)
        if validarabdomenB==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return abdomenB
    def clean_piernaD(self):
        piernaD=self.cleaned_data['piernaD']
        validarpiernaD=re.search(r'^[0-9,]{1,7}$',piernaD, flags=re.MULTILINE)
        if validarpiernaD==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return piernaD
    def clean_piernaI(self):
        piernaI=self.cleaned_data['piernaI']
        validarpiernaI=re.search(r'^[0-9,]{1,7}$',piernaI, flags=re.MULTILINE)
        if validarpiernaI==None:
            raise ValidationError("Error. Solo se permite ingresar caracteres númericos")
        return piernaI
    
    class Meta: 
        model=ControlMedidas
        fields='__all__'
        widgets={
            'fecha':forms.TextInput(attrs={'class':'form-control','type':'date','placeholder':'Ingrese la fecha sus medidas','required':False}),
            'brazoD':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
            'brazoI':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
            'abdomenA':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
            'cintura':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
            'abdomenB':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
            'piernaD':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
            'piernaI':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la medida'}),
         }
        