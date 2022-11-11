from django.shortcuts import render ,redirect
from Apps.Clientes.models import *
from Apps.Clientes.forms import *

# Create your views here.

#Listar Clientes
def listarCliente(request):
    listarCliente=Clientes.objects.filter()
    contexto={"cliente":listarCliente}
    return render(request,"Clientes/Clientes.html",contexto)

def crearCliente(request): 
    if request.method=='POST':
        formulario_cliente=FormularioCliente(request.POST)
        if formulario_cliente.is_valid():
            formulario_cliente.save()
            return redirect('/Clientes/')
    else: 
        formulario_cliente=FormularioCliente()
    contexto={'formulario_cliente':formulario_cliente}
    return render(request,'Clientes/Crear-Cliente.html',contexto)

def editarCliente(request, id):
    cliente=Clientes.objects.get(idCliente=id)
    if request.method=='GET':
        formulario_cliente=FormularioCliente(instance=cliente)
    else:
        formulario_cliente=FormularioCliente(request.POST,instance=cliente)
        if formulario_cliente.is_valid():
            formulario_cliente.save()
            return redirect('/Clientes/')
    contexto={'formulario_cliente':formulario_cliente}
    return render(request,'Clientes/Editar-Cliente.html',contexto)

def detalleCliente(request, id):
    mostrar=Clientes.objects.filter(idCliente=id).first()
    corporal=EsteticoCorporal.objects.filter(idCliente=id) 
    facial=EsteticoFacial.objects.filter(idCliente=id) 
    contexto={"mostrar":mostrar,"corporal":corporal,"facial":facial}
    return render(request,"Clientes/Detalles-Clientes.html",contexto)

def crearCorporal(request,id):
    if request.method=='POST':
        formulario_corporal=FormularioCorporal(request.POST)
        if formulario_corporal.is_valid():
            formulario_corporal.save()
            return redirect('Clientes.Ver-detalle',id)
    else: 
        formulario_corporal=FormularioCorporal()
    contexto={'formulario_corporal':formulario_corporal,"idCliente":id}
    return render(request,'Clientes/Crear-Corporal.html',contexto)

def crearFacial(request,id):
    if request.method=='POST':
        formulario_facial=FormularioFacial(request.POST)
        if formulario_facial.is_valid():
            formulario_facial.save()
            return redirect('Clientes.Ver-detalle',id)
    else: 
        formulario_facial=FormularioFacial()
    contexto={'formulario_facial':formulario_facial,"idCliente":id}
    return render(request,'Clientes/Crear-Facial.html',contexto)

def VerDetalleCorporal(request, id):
    mostrar=EsteticoCorporal.objects.filter(idCorporal=id).first()
    medidas=ControlMedidas.objects.filter(idCorporal=id)
    contexto={"mostrar":mostrar,"medidas":medidas}
    return render(request,"Clientes/Historial-Corporal.html",contexto)

def VerDetalleFacial(request, id):
    mostrar=EsteticoFacial.objects.filter(idFacial=id).first()
    contexto={"mostrar":mostrar}
    return render(request,"Clientes/Historial-Facial.html",contexto)

def crearControlMedidas(request,id):
    if request.method=='POST':
        formulario_medidas=FormularioMedidas(request.POST)
        if formulario_medidas.is_valid():
            formulario_medidas.save()
            return redirect('Clientes.Ver-Detalles.Corporal',id)
    else: 
        formulario_medidas=FormularioMedidas()
    contexto={'formulario_medidas':formulario_medidas,"idCorporal":id}
    return render(request,'Clientes/Crear-Medidas.html',contexto)


def crearPagosSesionesFacial(request,id):
    crearIdF=EsteticoFacial.objects.get(idFacial=id)
    sesionesFecha=request.GET['fecha']
    sesionesC=request.GET['secionesC']
    sesionesValor=request.GET['valor']
    sesionesAbono=request.GET['abono']

    if sesionesAbono< sesionesValor:
        seciones=Sesiones(fecha=sesionesFecha,Nseciones=sesionesC,valor=sesionesValor,abono=sesionesAbono,estado="Por pagar",idFacial=crearIdF)
        seciones.save()
    elif sesionesAbono> sesionesValor:
        seciones=Sesiones(fecha=sesionesFecha,Nseciones=sesionesC,valor=sesionesValor,abono=sesionesAbono,estado="Devolver",idFacial=crearIdF)
        seciones.save()
    else:
        seciones=Sesiones(fecha=sesionesFecha,Nseciones=sesionesC,valor=sesionesValor,abono=sesionesAbono,estado="Pagado",idFacial=crearIdF)
        seciones.save()

    return redirect("Clientes.Ver-Detalles.Facial",id)

def editarPagosSesionesFacial(request,id):
    mostrar=Sesiones.objects.filter(idSesiones=id).first()
    contexto={"mostrar":mostrar}
    return render(request,"Clientes/Editar-Pagos-Sesiones-Facial.html",contexto)

def actualizarPagosSesionesFacial(request, id):
    sesionesFecha=request.GET['fecha']
    sesionesC=request.GET['secionesC']
    sesionesValor=request.GET['valor']
    sesionesAbono=request.GET['abono']

    if sesionesAbono< sesionesValor:
        actualizar=Sesiones.objects.get(idSesiones=id)
        actualizar.fecha=sesionesFecha
        actualizar.Nseciones=sesionesC
        actualizar.valor=sesionesValor
        actualizar.abono=sesionesAbono
        actualizar.estado="Por pagar"
        actualizar.save()
    elif sesionesAbono> sesionesValor:
        actualizar=Sesiones.objects.get(idSesiones=id)
        actualizar.fecha=sesionesFecha
        actualizar.Nseciones=sesionesC
        actualizar.valor=sesionesValor
        actualizar.abono=sesionesAbono
        actualizar.estado="Devolver"
        actualizar.save()
    else:
        actualizar=Sesiones.objects.get(idSesiones=id)
        actualizar.fecha=sesionesFecha
        actualizar.Nseciones=sesionesC
        actualizar.valor=sesionesValor
        actualizar.abono=sesionesAbono
        actualizar.estado="Pagado"
        actualizar.save()

    return redirect("Clientes.Ver-Detalles.Facial",id)

def editarPagosSesionesCorporal(request,id):
    mostrar=Sesiones.objects.filter(idSesiones=id).first()
    contexto={"mostrar":mostrar}
    return render(request,"Clientes/Editar-Pagos-Sesiones-Corporal.html",contexto)

def cantidadClientes(request):
    totalClientes = Clientes.objects.count().filter()
    context= {"totalClientes":totalClientes}
    return render(request,"partials/content.html", context)

def actualizarPagosSesionesCorporal(request, id):
    sesionesFecha=request.GET['fecha']
    sesionesC=request.GET['secionesC']
    sesionesValor=request.GET['valor']
    sesionesAbono=request.GET['abono']

    if sesionesAbono< sesionesValor:
        actualizar=Sesiones.objects.get(idSesiones=id)
        actualizar.fecha=sesionesFecha
        actualizar.Nseciones=sesionesC
        actualizar.valor=sesionesValor
        actualizar.abono=sesionesAbono
        actualizar.estado="Por pagar"
        actualizar.save()
    elif sesionesAbono> sesionesValor:
        actualizar=Sesiones.objects.get(idSesiones=id)
        actualizar.fecha=sesionesFecha
        actualizar.Nseciones=sesionesC
        actualizar.valor=sesionesValor
        actualizar.abono=sesionesAbono
        actualizar.estado="Devolver"
        actualizar.save()
    else:
        actualizar=Sesiones.objects.get(idSesiones=id)
        actualizar.fecha=sesionesFecha
        actualizar.Nseciones=sesionesC
        actualizar.valor=sesionesValor
        actualizar.abono=sesionesAbono
        actualizar.estado="Pagado"
        actualizar.save()

