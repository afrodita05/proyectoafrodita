from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from Apps.Clientes.models import Clientes
from django.views.generic import ListView
# Create your views here.

<<<<<<< HEAD
def cliente(request):
    cliente=Clientes.objects.filter()
    clientes={"cliente":cliente}
=======

#Listar Clientes
def cliente(request):
    listarCliente=Clientes.objects.filter()
    clientes={"cliente":listarCliente}
>>>>>>> clientes
    return render(request,"pages/Clientes.html",clientes)

def formularioCliente(request):
    return render(request,"pages/Crear-Cliente.html")

def crearCliente(request):
    print("hola, request ",request.POST['sexo'])
    nombreCliente=request.POST['nombre']
    documentoCliente=request.POST['documento']
    sexoCliente=request.POST['sexo']
    telefonoCliente=request.POST['telefono']
    direccionCliente=request.POST['direccion']
    correoCliente=request.POST['correo']
    fechaNacimientoCliente=request.POST['fechaNacimiento']
    estadoCivilCliente=request.POST['estadoCivil']
    numeroHijosCliente=request.POST['numeroHijos']
    clientes=Clientes(nombre=nombreCliente,documento=documentoCliente,sexo=sexoCliente,telefono=telefonoCliente,direccion=direccionCliente,correo=correoCliente,fechaNacimiento=fechaNacimientoCliente,estadoCivil=estadoCivilCliente,numeroHijos=numeroHijosCliente)
    clientes.save()
    return redirect("/Clientes/") #url 
<<<<<<< HEAD
=======

def editarCliente(request, id):
    mostrar=Clientes.objects.filter(idCliente=id).first()
    clientes={"mostrar":mostrar}
    return render(request,"pages/Editar-Cliente.html",clientes)
    
def actualizarCliente(request, id):
    nombreCliente=request.GET['nombre']
    documentoCliente=request.GET['documento']
    sexoCliente=request.GET['sexo']
    telefonoCliente=request.GET['telefono']
    direccionCliente=request.GET['direccion']
    correoCliente=request.GET['correo']
    fechaNacimientoCliente=request.GET['fechaNacimiento']
    estadoCivilCliente=request.GET['estadoCivil']
    numeroHijosCliente=request.GET['numeroHijos']
    actualizar=Clientes.objects.get(idCliente=id)
    actualizar.nombre=nombreCliente
    actualizar.documento=documentoCliente
    actualizar.sexo=sexoCliente
    actualizar.telefono=telefonoCliente
    actualizar.direccion=direccionCliente
    actualizar.correo=correoCliente
    actualizar.fechaNacimiento=fechaNacimientoCliente
    actualizar.estadoCivil=estadoCivilCliente
    actualizar.numeroHijos=numeroHijosCliente
    actualizar.save()
    return redirect("/Clientes/")
>>>>>>> clientes
    

# class Clienteview(TemplateView):
    
#     pass
# Clientes = Clienteview.as_view(
#     template_name="pages/Clientes.html"
# )
# Detalle_Cliente = Clienteview.as_view(
#     template_name="pages/Detalles-Clientes.html"
# )
# Historial_Corporal = Clienteview.as_view(
#     template_name="pages/Historial-Corporal.html"
# )
# Historial_Facial = Clienteview.as_view(
#     template_name="pages/Historial-Facial.html"
# )

# class ClientesH(ListView):
#     model=Clientes
#     template_name='pages/Clientes.html'

#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         listarcliente=Clientes.objects.filter()
#         context['listar']=listarcliente
#         return context

# class CrearCliente(ListView):
#     model=Clientes
#     template_name='pages/Crear-Cliente.html'

#     def post(self, request, *args, **kwargs):
#         nombreCliente=request.POST['nombre']
#         documentoCliente=request.POST['documento']
#         sexoCliente=request.POST['sexo']
#         telefonoCliente=request.POST['telefono']
#         direccionCliente=request.POST['direccion']
#         correoCliente=request.POST['correo']
#         fechaNacimientoCliente=request.POST['fechaNacimiento']
#         estadoCivilCliente=request.POST['estadoCivil']
#         numeroHijosCliente=request.POST['numeroHijos']
#         clientes=Clientes(nombre=nombreCliente,documento=documentoCliente,sexo=sexoCliente,telefono=telefonoCliente,direccion=direccionCliente,correo=correoCliente,fechaNacimiento=fechaNacimientoCliente,estadoCivil=estadoCivilCliente,numeroHijos=numeroHijosCliente)
#         clientes.save()
#         return redirect('pages/Clientes.html')