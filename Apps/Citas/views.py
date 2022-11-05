from django.shortcuts import render, redirect
from Apps.Citas.models import *
from Apps.Citas.forms import *
from Apps.Clientes.models import Clientes
from django import forms

# Create your views here.

def listarCita(request):
    citas=Citas.objects.filter()
    contexto={"citas":citas}
    return render(request,"Citas/Citas.html",contexto)

def verificarDocumento(request):
    clienteDocumento= request.POST.get('documento')
    existe=Clientes.objects.filter(documento=clienteDocumento).exists()
    idCliente = Clientes.objects.filter(documento = clienteDocumento).values_list('idCliente', flat=True).first()
    
    if existe: 
        return redirect('crear-Citas',idCliente)

    else:
        error="El documento que ingreso no está registrado en el sistema"
        contexto={"error":error}
        return render(request,'Citas/VerificarDocumento.html',contexto)
    
    

def crearCita(request,id):
    if request.method=='POST':
        formulario_citas=FormularioCitas(request.POST)
        if formulario_citas.is_valid():
            formulario_citas.save()
            return redirect('/Cita/')
    else: 
        formulario_citas=FormularioCitas()
        
    contexto={'formulario_citas':formulario_citas,'idCliente':id}
    return render(request,'Citas/Crear-Cita.html',contexto)
    
    
    
def editarCita(request,id):
    citas=Citas.objects.get(idCita=id)
    if request.method=='GET':
        formulario_citas=FormularioCitas(instance=citas)
    else:
        formulario_citas=FormularioCitas(request.POST,instance=citas)
        if formulario_citas.is_valid():
            formulario_citas.save()
            return redirect('/Cita/')
    contexto={'formulario_citas':formulario_citas}
    return render(request,'Citas/Editar-Cita.html',contexto)


def verDetalleCita(request, id):
    cliente=Clientes.objects.filter(idCliente=id).first()
    agendaCosto=AgendaCosto.objects.filter(idCliente=id)
    contexto={"agendaCosto":agendaCosto,"cliente":cliente}
    return render(request,"Citas/VerDetalleCita.html",contexto)

def crearAgendaCosto(request, id):

    if request.method=='POST':
        formulario_agenda_costo=FormularioAgendaCosto(request.POST)
        if formulario_agenda_costo.is_valid():
            formulario_agenda_costo.save()
            return redirect('verDetalle-Cita', id)
    else: 
        formulario_agenda_costo=FormularioAgendaCosto()
    
    contexto={'formulario_agenda_costo':formulario_agenda_costo,'idCliente':id}
    return render(request,'Citas/CrearCosto.html',contexto)

def editarAgendaCosto(request,id):
    agendaCosto=AgendaCosto.objects.get(idAgendaCosto=id)
    if request.method=='GET':
        formulario_agenda_costo=FormularioAgendaCosto(instance=agendaCosto)
    else:
        formulario_agenda_costo=FormularioAgendaCosto(request.POST,instance=agendaCosto)
        if formulario_agenda_costo.is_valid():
            formulario_agenda_costo.save()
            return redirect('verDetalle-Cita', id)
    contexto={'formulario_agenda_costo':formulario_agenda_costo}
    return render(request,'Citas/EditarCosto.html',contexto)

def verDetalleCosto(request, id):
    agendaCosto=AgendaCosto.objects.filter(idAgendaCosto=id).first()
    agendaFecha=AgendaFecha.objects.filter(idAgendaCosto=id)
    cliente=Clientes.objects.filter(idCliente=id).first()
    contexto={"agendaFecha":agendaFecha,"agendaCosto":agendaCosto,"cliente":cliente}
    return render(request,"Citas/VerDetalleCosto.html",contexto)

def crearAgendaFecha(request, id):
    if request.method=='POST':
        formulario_agenda_fecha=FormularioAgendaFecha(request.POST)
        if formulario_agenda_fecha.is_valid():
            formulario_agenda_fecha.save()
            return redirect('verDetalle-Costo', id)
    else: 
        formulario_agenda_fecha=FormularioAgendaFecha()

    agendacosto=AgendaCosto.objects.filter(idAgendaCosto=id)
    for listar in agendacosto:

        clienteCosto=listar.costo
        clienteAbono=listar.abono


        if clienteAbono<clienteCosto:
            estado="Por pagar"
            contexto={'estado':estado,'formulario_agenda_fecha':formulario_agenda_fecha,'idAgendaCosto':id}
            return render(request,'Citas/CrearFecha.html',contexto)
        elif clienteAbono==clienteCosto:
            estado="Pagado"
            contexto={'estado':estado,'formulario_agenda_fecha':formulario_agenda_fecha,'idAgendaCosto':id}
            return render(request,'Citas/CrearFecha.html',contexto)
        else :
            estado="Excedente"
            contexto={'estado':estado,'formulario_agenda_fecha':formulario_agenda_fecha,'idAgendaCosto':id}
            return render(request,'Citas/CrearFecha.html',contexto)

        
    contexto={'formulario_agenda_fecha':formulario_agenda_fecha}
    return render(request,'Citas/CrearFecha.html',contexto)

def editarFechaAgenda(request,id):
    fecha=AgendaFecha.objects.get(idAgendaFecha=id)
    if request.method=='GET':
         formulario_agenda_fecha=FormularioAgendaFecha(instance=fecha)
    else:
        formulario_agenda_fecha=FormularioAgendaFecha(request.POST,instance=fecha)
        if formulario_agenda_fecha.is_valid():
            formulario_agenda_fecha.save()
            return redirect('verDetalle-Costo', id)
    contexto={'formulario_agenda_fecha': formulario_agenda_fecha}
    return render(request,'Citas/EditarFecha.html',contexto)


        # agendafecha=AgendaFecha.objects.filter(idAgendaCosto=id)

        # contador=0
        # while contador<agendafecha:
        #     contador+=1

        
        # if contador==clienteSesiones:
        #     error='El número de sesiones es superior'
        #     contexto={'error':error}
        #     render(request,'Citas/crearFecha.html',contexto)























