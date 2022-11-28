from django.shortcuts import render, redirect
from Apps.Citas.models import *
from Apps.Citas.forms import *
from Apps.Clientes.models import Clientes
from Apps.Servicios.models import *
from Apps.Insumos.models import *
from django import forms
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
# Create your views here.

@permission_required('Citas.view_citas',raise_exception=True) 
def listarCita(request):
    citas=Citas.objects.filter()
    contexto={"citas":citas}
    return render(request,"Citas/Citas.html",contexto)

@permission_required('Citas.view_citas',raise_exception=True) 
def rutaVCita(request):
    clientes=Clientes.objects.filter()
    context={"clientes":clientes}
    return render(request,"Citas/VerificarDocumento.html",context)

@permission_required('Citas.view_citas',raise_exception=True) 
def verificarDocumento(request):
    clienteDocumento= request.POST.get('documento')
    existe=Clientes.objects.filter(documento=clienteDocumento).exists()
    idCliente = Clientes.objects.filter(documento = clienteDocumento).values_list('idCliente', flat=True).first()
    
    if existe: 
        return redirect('crear-Citas',idCliente)

    else:
        
        error="El documento que ingresó no está registrado en el sistema"
        contexto={"error":error}
        return render(request,'Citas/VerificarDocumento.html',contexto)

@permission_required('Citas.view_citas',raise_exception=True)  
def crearCita(request,id):
    if request.method=='POST':
        formulario_citas=FormularioCitas(request.POST)
        if formulario_citas.is_valid():
            idServicioo=request.POST.get('idServicio')
            print("El nombre esssss: ",idServicioo)
            idServicioo=int(idServicioo)
            idServicio = Servicios.objects.filter(idServicio=idServicioo).values_list('idServicio', flat= True).first()
            if Servicios.objects.filter(idServicio=idServicio).values_list('estado', flat= True).first() == 0:
                desactivado="El servicio escogido está desactivado. Para crear una cita con este servicio, actívalo desde la edición de servicios."
                contexto={'formulario_citas':formulario_citas,'idCliente':id, 'desactivado':desactivado}
                return render(request,'Citas/Crear-Cita.html',contexto)
            else:
                formulario_citas.save()
                return redirect('/Cita/')
    else: 
        formulario_citas=FormularioCitas()
        
    contexto={'formulario_citas':formulario_citas,'idCliente':id}
    return render(request,'Citas/Crear-Cita.html',contexto)

@permission_required('Citas.view_citas',raise_exception=True) 
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

@permission_required('Citas.view_citas',raise_exception=True) 
def verDetalleCita(request, id):
    

    idCliente = Citas.objects.filter(idCita=id).values_list('idCliente', flat=True).first()
    idCliente= int(idCliente)
    cliente = Clientes.objects.get(idCliente=idCliente)
    cita=Citas.objects.get(idCita=id)
    agendaCosto=AgendaCosto.objects.filter(idCita=id)
    contexto={"agendaCosto":agendaCosto,"cita":cita}
    return render(request,"Citas/VerDetalleCita.html",contexto)

@permission_required('Citas.view_citas',raise_exception=True) 
def crearAgendaCosto(request, id):
    
    if request.method=='POST':
        formulario_agenda_costo=FormularioAgendaCosto(request.POST)
        
        if formulario_agenda_costo.is_valid():
            
            valorPagoServicio=request.POST.get('costo')
            valorPagoServicio= int(valorPagoServicio)
            idServicio= Citas.objects.filter(idCita = id).values_list('idServicio', flat=True).first() #Obtengo el id del servicio basado en el id de la cita
            idServicio=int(idServicio) #Lo convierto a integer
            
            valorServicio = Servicios.objects.filter(idServicio = idServicio).values_list('valor', flat= True).first() #encuentro el valor del servicior
            valorServicio = int(valorServicio) #lo convierto a integer
            proporcionServicio= valorPagoServicio/valorServicio #obtengo la proporción del servicio: el valor pagado dividido el valor original = cuántas veces estoy pagando el servicio
            insumosServicio = Servicios_Insumo.objects.filter(idServicio_id=idServicio).values_list('idInsumo', flat= True) #obtengo los id de los insumos usados por este servicio
            insumos = Servicios_Insumo.objects.filter() #Obtengo una lista de todos los insumos mencionados anteriormente
            contador = 0
            listaIDs=[]
            
            

            for insumos.idInsumo in insumosServicio:
                
                idInsumo = insumos.idInsumo
                
                cantidadInsumo = Insumo.objects.filter(idInsumo=idInsumo).values_list('cantidad', flat= True).first()
                
                cantidadServicio = Servicios_Insumo.objects.filter(Q(idInsumo=idInsumo) & Q(idServicio=idServicio)).values_list('cantidadUsada', flat= True).first() #Anidar condiciones: No basta con que la cantidad usada coincida en id de insumo, sino también en idServicios_Insumo.
                cantidadInsumo=int(cantidadInsumo)
                cantidadServicio=int(cantidadServicio)

                if cantidadServicio<=cantidadInsumo:
                    listaIDs.append(idInsumo)


                else:
                    listaIDs.clear()
                    formulario_agenda_costo=FormularioAgendaCosto()
                    insuficiente="No hay insumos suficientes para realizar el servicio."
                    contexto={'formulario_agenda_costo':formulario_agenda_costo,'idCita':id, 'errorCantidad':insuficiente}
                    return render(request,'Citas/CrearCosto.html',contexto)  

            for insumos.idInsumo in insumosServicio:

                idInsumoActual=listaIDs[contador]
                
                nombreInsumo = Insumo.objects.filter(idInsumo=idInsumoActual).values_list('nombreInsumo', flat= True).first()
                nombreInsumo= str(nombreInsumo)
                cantidadInsumo = Insumo.objects.filter(idInsumo=idInsumoActual).values_list('cantidad', flat= True).first()
                
               
                cantidadServicio = Servicios_Insumo.objects.filter(Q(idInsumo=idInsumoActual) & Q(idServicio=idServicio)).values_list('cantidadUsada', flat= True).first() #Anidar condiciones: No basta con que la cantidad usada coincida en id de insumo, sino también en idServicios_Insumo.
                cantidadInsumo=int(cantidadInsumo)
                cantidadServicio=int(cantidadServicio)

                cantidadFinal= cantidadInsumo-(cantidadServicio*proporcionServicio)
                tipoUnidad = Insumo.objects.filter(idInsumo=idInsumoActual).values_list('tipoUnidad', flat= True).first()
                estado = Insumo.objects.filter(idInsumo=idInsumoActual).values_list('estado', flat= True).first()
                tipoUnidad = str(tipoUnidad)
                estado= str(estado)

                insumos = Insumo(idInsumo=idInsumoActual, cantidad=cantidadFinal, nombreInsumo=nombreInsumo, tipoUnidad= tipoUnidad, estado= estado)
                insumos.save()
                contador=contador+1



            formulario_agenda_costo.save()
            return redirect('verDetalle-Cita', id)        
            
    else: 
        formulario_agenda_costo=FormularioAgendaCosto()
        
    contexto={'formulario_agenda_costo':formulario_agenda_costo,'idCita':id}
    return render(request,'Citas/CrearCosto.html',contexto)

@permission_required('Citas.view_citas',raise_exception=True) 
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

@permission_required('Citas.view_citas',raise_exception=True) 
def verDetalleCosto(request, id):
    agendaCosto=AgendaCosto.objects.filter(idAgendaCosto=id).first()
    agendaFecha=AgendaFecha.objects.filter(idAgendaCosto=id)
    cliente=Clientes.objects.filter(idCliente=id).first()
    contexto={"agendaFecha":agendaFecha,"agendaCosto":agendaCosto,"cliente":cliente}
    
    return render(request,"Citas/VerDetalleCosto.html",contexto)

@permission_required('Citas.view_citas',raise_exception=True) 
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

@permission_required('Citas.view_citas',raise_exception=True) 
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























