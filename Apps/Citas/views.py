from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Citas.models import Clientes, Citas
from Apps.Servicios.models import Servicios
# Create your views here.


def crearCita(request):
    servicios=Servicios.objects.filter()  
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

    idCliente=clientes.idCliente
    servicioCita=request.POST['servicios1'] 
    idServicio = Servicios.objects.filter(nServicio=servicioCita).values('idServicio')[0]['idServicio']     
    fechaCita=request.POST['fechaCita']    
    citas=Citas(fecha=fechaCita,idServicio_id=idServicio,idCliente_id=idCliente)
    citas.save()
    return redirect("Cita")

    
def formularioCita(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}   
    return render(request,"Citas/Crear-Cita.html", context)


def listarCita(request):   
    listarCita=Citas.objects.filter()
    listarClientes=Clientes.objects.filter()    
    servicio=Servicios.objects.filter()
    context={"crcita":listarCita,"lrClientes":listarClientes,"servicio":servicio,}

    return render(request,"Citas/Citas.html", context)


def editarCita(request, id):
    servicio=Servicios.objects.filter()
    ver=Citas.objects.filter(idCitas=id).first()
    context={"ver":ver,"servicio":servicio}
    return render(request,"Citas/Editar-Cita.html",context)

def editarCliente(request, id):
    mostrar=Clientes.objects.filter(idCliente=id).first()    
    context={"mostrar":mostrar}
    return render(request,"editarCliente.html",context)

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
    actualizar.sexo=sexoCliente
    actualizar.documento=documentoCliente
    actualizar.fechaNacimiento=fechaNacimientoCliente    
    actualizar.telefono=telefonoCliente
    actualizar.direccion=direccionCliente
    actualizar.correo=correoCliente    
    actualizar.estadoCivil=estadoCivilCliente
    actualizar.numeroHijos=numeroHijosCliente
    actualizar.save()

    return redirect("/listarCita/")
   
def actualizarCita(request, id):
    fechaCita=request.GET['fechaCita']
    servicioCita=request.GET['servicios1']
    actualizar=Citas.objects.get(idCitas=id)
    idServicio = Servicios.objects.filter(nServicio=servicioCita).values('idServicio')[0]['idServicio']
    actualizar.fecha=fechaCita
    actualizar.idServicio_id=idServicio
    actualizar.save()

    return redirect("/listarCita/")

def servicio(request):
    servicio=Servicios.objects.filter()
    context={"lServicio":servicio}
    return render(request,"/listarCita/",context)




# class Citaview(TemplateView):
#     pass

# Citas = Citaview.as_view(
#     template_name="Citas/Citas.html"
# )
# Crear_Cita = Citaview.as_view(
#     template_name="Citas/Crear-Cita.html"
# )
# Editar_Cita = Citaview.as_view(
#     template_name="Citas/Editar-Cita.html"
# )