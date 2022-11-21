from django.shortcuts import render, redirect
from Apps.Citas.models import *
from Apps.Citas.forms import *
from Apps.Clientes.models import Clientes
from Apps.Servicios.models import *
from Apps.Insumos.models import *
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
    

    idCliente = Citas.objects.filter(idCita=id).values_list('idCliente', flat=True).first()
    idCliente= int(idCliente)
    cliente = Clientes.objects.get(idCliente=idCliente)
    cita=Citas.objects.get(idCita=id)
    agendaCosto=AgendaCosto.objects.filter(idCita=id)
    contexto={"agendaCosto":agendaCosto,"cita":cita}
    return render(request,"Citas/VerDetalleCita.html",contexto)

def crearAgendaCosto(request, id):
    print(id, "ESTA ES LA ID DE CITA")
    
    if request.method=='POST':
        formulario_agenda_costo=FormularioAgendaCosto(request.POST)
        
        if formulario_agenda_costo.is_valid():
            formulario_agenda_costo.save()
            valorPagoServicio=request.POST.get('costo')
            valorPagoServicio= int(valorPagoServicio)
            idServicio= Citas.objects.filter(idCita = id).values_list('idServicio', flat=True).first() #Obtengo el id del servicio basado en el id de la cita
            idServicio=int(idServicio) #Lo convierto a integer
            print("El id del servicio será: ", idServicio)
            valorServicio = Servicios.objects.filter(idServicio = idServicio).values_list('valor', flat= True).first() #encuentro el valor del servicior
            valorServicio = int(valorServicio) #lo convierto a integer
            proporcionServicio= valorPagoServicio/valorServicio #obtengo la proporción del servicio: el valor pagado dividido el valor original = cuántas veces estoy pagando el servicio
            insumosServicio = Servicios_Insumo.objects.filter(idServicio_id=idServicio).values_list('idInsumo', flat= True) #obtengo los id de los insumos usados por este servicio
            insumos = Servicios_Insumo.objects.filter() #Obtengo una lista de todos los insumos mencionados anteriormente
            contador=0
            

            print("Los id de los servicios son: ", insumosServicio)
            print("Los valores son: ")

            for insumos.idInsumo in insumosServicio:
                
                idInsumo = insumos.idInsumo
                print("El id del insumo para el caso es: ",idInsumo)
                cantidadInsumo = Insumo.objects.filter(idInsumo=idInsumo).values_list('cantidad', flat= True).first()
                print("La cantidad del insumo para el caso es: ", cantidadInsumo)
                cantidadServicio = Servicios_Insumo.objects.filter(idInsumo=idInsumo).values_list('cantidadUsada', flat= True).first()
                cantidadInsumo=int(cantidadInsumo)
                cantidadServicio=int(cantidadServicio)
                print("La nueva cantidad de insumo es: ", cantidadInsumo, ". Y la nueva cantidad de servicio es: ", cantidadServicio)
                nombreInsumo = Insumo.objects.filter(idInsumo=idInsumo).values_list('nombreInsumo', flat= True).first()
                nombreInsumo= str(nombreInsumo)
                cantidadFinal= cantidadInsumo-(cantidadServicio*proporcionServicio)
                print("El resultante es: ", cantidadFinal)
                insumos =  Insumo(idInsumo=idInsumo, cantidad=cantidadFinal, nombreInsumo=nombreInsumo)
                insumos.save()
                    




            #PASO 3:
            #Dividir el costo de valorPagoServicio sobre el costo del servicio
            #Esto dará la cantidad de veces que el cobro vale el servicio
            #Descontar los insumos del servicio con base en este valor

            print(valorPagoServicio)
            return redirect('verDetalle-Cita', id)
            
    else: 
        formulario_agenda_costo=FormularioAgendaCosto()
        
    contexto={'formulario_agenda_costo':formulario_agenda_costo,'idCita':id}
    return render(request,'Citas/CrearCosto.html',contexto)


def editarAgendaCosto(request,id):
    agendaCosto=AgendaCosto.objects.get(idAgendaCosto=id)
    if request.method=='GET':
        formulario_agenda_costo=FormularioAgendaCosto(instance=agendaCosto)
    else:
        formulario_agenda_costo=FormularioAgendaCosto(request.POST,instance=agendaCosto)
        if formulario_agenda_costo.is_valid():
            formulario_agenda_costo.save()
            return redirect('verDetalle-Cita', agendaCosto.idCita.idCita)
    contexto={'formulario_agenda_costo':formulario_agenda_costo}
    return render(request,'Citas/EditarCosto.html',contexto)

def verDetalleCosto(request, id):
    agendaCosto=AgendaCosto.objects.filter(idAgendaCosto=id).first()
    agendaFecha=AgendaFecha.objects.filter(idAgendaCosto=id)
    cliente=Clientes.objects.filter(idCliente=id).first()
    contexto={"agendaFecha":agendaFecha,"agendaCosto":agendaCosto,"cliente":cliente}
    print("DETALLE", contexto)
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
    print("COSTO", agendacosto)
    print("IDE",id)
    print("Valido",formulario_agenda_fecha.is_valid())
    for listar in agendacosto:

        clienteCosto=int(listar.costo)
        clienteAbono=int(listar.abono)

        
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
            return redirect('verDetalle-Costo', fecha.idAgendaCosto.idAgendaCosto)
    contexto={'formulario_agenda_fecha': formulario_agenda_fecha}
    return render(request,'Citas/EditarFecha.html',contexto)


        # agendafecha=AgendaFecha.objects.filter(idAgendaCosto=id) #Toma todos los idAgendaCosto relacionados al actual. Si el actual es 2, debe tomar todos los asociados al 2.

        #  contador=0
        #  while contador<agendafecha: #Sumará de uno en uno hasta llegar al número límite
        #      contador+=1

        
         
        #  error='El número de sesiones es superior' #Al terminar el conteo, saltará un error: se excedió la cantidad
        #  contexto={'error':error}
        #  render(request,'Citas/crearFecha.html',contexto)























