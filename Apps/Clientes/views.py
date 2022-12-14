from django.shortcuts import render ,redirect
from Apps.Clientes.models import *
from Apps.Clientes.forms import *
from django.contrib.auth.decorators import permission_required
# Create your views here.

#Listar Clientes
@permission_required('Clientes.view_clientes',raise_exception=True) 
def listarCliente(request):
    listarCliente=Clientes.objects.filter()
    contexto={"cliente":listarCliente}
    return render(request,"Clientes/Clientes.html",contexto)

@permission_required('Clientes.view_clientes',raise_exception=True) 
def crearCliente(request): 
    if request.method=='POST':
        formulario_cliente=FormularioCliente(request.POST)
        if formulario_cliente.is_valid():
            documento=formulario_cliente.cleaned_data.get('documento')
            existe=Clientes.objects.filter(documento=documento).exists()
            if existe:
                mensaje_error="El documento ya existe"
                contexto={'formulario_cliente':formulario_cliente,"mensaje_error":mensaje_error}
                return render(request,'Clientes/Crear-Cliente.html',contexto)
            else:
                formulario_cliente.save()
                return redirect('/Clientes/')
    else: 
        formulario_cliente=FormularioCliente()
    contexto={'formulario_cliente':formulario_cliente}
    return render(request,'Clientes/Crear-Cliente.html',contexto)

@permission_required('Clientes.view_clientes',raise_exception=True) 
def editarCliente(request, id):
    cliente=Clientes.objects.get(idCliente=id)
    documento=cliente.documento
    if request.method=='GET':
        formulario_cliente=FormularioCliente(instance=cliente)
    else:
        formulario_cliente=FormularioCliente(request.POST,instance=cliente)
        if formulario_cliente.is_valid():
            inputDocumento=formulario_cliente.cleaned_data.get('documento')
            existe=Clientes.objects.filter(documento=inputDocumento).exclude(idCliente=id).count()
            if existe==0:
                formulario_cliente.save()
                return redirect('/Clientes/')
            else:
                mensaje_error="El documento ya existe"
                contexto={'formulario_cliente':formulario_cliente,"mensaje_error":mensaje_error}
                return render(request,'Clientes/Editar-Cliente.html',contexto)
                  
    contexto={'formulario_cliente':formulario_cliente,"documento":documento}
    return render(request,'Clientes/Editar-Cliente.html',contexto)

@permission_required('Clientes.view_clientes',raise_exception=True) 
def detalleCliente(request, id):
    mostrar=Clientes.objects.filter(idCliente=id).first()
    corporal=EsteticoCorporal.objects.filter(idCliente=id) 
    facial=EsteticoFacial.objects.filter(idCliente=id) 
    contexto={"mostrar":mostrar,"corporal":corporal,"facial":facial}
    return render(request,"Clientes/Detalles-Clientes.html",contexto)

@permission_required('Clientes.view_clientes',raise_exception=True) 
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

@permission_required('Clientes.view_clientes',raise_exception=True) 
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

@permission_required('Clientes.view_clientes',raise_exception=True) 
def VerDetalleCorporal(request, id):
    mostrar=EsteticoCorporal.objects.filter(idCorporal=id).first()
    documentoCosto=mostrar.idCliente.idCliente
    
    medidas=ControlMedidas.objects.filter(idCorporal=id)
    contexto={"mostrar":mostrar,"medidas":medidas,"documentoCosto":documentoCosto}
    return render(request,"Clientes/Historial-Corporal.html",contexto)

@permission_required('Clientes.view_clientes',raise_exception=True) 
def VerDetalleFacial(request, id):
    mostrar=EsteticoFacial.objects.filter(idFacial=id).first()
    documentoCosto=mostrar.idCliente.idCliente
    contexto={"mostrar":mostrar,"documentoCosto":documentoCosto}
    return render(request,"Clientes/Historial-Facial.html",contexto)

@permission_required('Clientes.view_clientes',raise_exception=True) 
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


# @permission_required('Clientes.view_clientes') 
# def crearPagosSesionesFacial(request,id):
#     crearIdF=EsteticoFacial.objects.get(idFacial=id)
#     sesionesFecha=request.GET['fecha']
#     sesionesC=request.GET['secionesC']
#     sesionesValor=request.GET['valor']
#     sesionesAbono=request.GET['abono']

#     if sesionesAbono< sesionesValor:
#         seciones=Sesiones(fecha=sesionesFecha,Nseciones=sesionesC,valor=sesionesValor,abono=sesionesAbono,estado="Por pagar",idFacial=crearIdF)
#         seciones.save()
#     elif sesionesAbono> sesionesValor:
#         seciones=Sesiones(fecha=sesionesFecha,Nseciones=sesionesC,valor=sesionesValor,abono=sesionesAbono,estado="Devolver",idFacial=crearIdF)
#         seciones.save()
#     else:
#         seciones=Sesiones(fecha=sesionesFecha,Nseciones=sesionesC,valor=sesionesValor,abono=sesionesAbono,estado="Pagado",idFacial=crearIdF)
#         seciones.save()

#     return redirect("Clientes.Ver-Detalles.Facial",id)

# @permission_required('Clientes.view_clientes') 
# def editarPagosSesionesFacial(request,id):
#     mostrar=Sesiones.objects.filter(idSesiones=id).first()
#     contexto={"mostrar":mostrar}
#     return render(request,"Clientes/Editar-Pagos-Sesiones-Facial.html",contexto)

# @permission_required('Clientes.view_clientes') 
# def actualizarPagosSesionesFacial(request, id):
#     sesionesFecha=request.GET['fecha']
#     sesionesC=request.GET['secionesC']
#     sesionesValor=request.GET['valor']
#     sesionesAbono=request.GET['abono']

#     if sesionesAbono< sesionesValor:
#         actualizar=Sesiones.objects.get(idSesiones=id)
#         actualizar.fecha=sesionesFecha
#         actualizar.Nseciones=sesionesC
#         actualizar.valor=sesionesValor
#         actualizar.abono=sesionesAbono
#         actualizar.estado="Por pagar"
#         actualizar.save()
#     elif sesionesAbono> sesionesValor:
#         actualizar=Sesiones.objects.get(idSesiones=id)
#         actualizar.fecha=sesionesFecha
#         actualizar.Nseciones=sesionesC
#         actualizar.valor=sesionesValor
#         actualizar.abono=sesionesAbono
#         actualizar.estado="Devolver"
#         actualizar.save()
#     else:
#         actualizar=Sesiones.objects.get(idSesiones=id)
#         actualizar.fecha=sesionesFecha
#         actualizar.Nseciones=sesionesC
#         actualizar.valor=sesionesValor
#         actualizar.abono=sesionesAbono
#         actualizar.estado="Pagado"
#         actualizar.save()

#     return redirect("Clientes.Ver-Detalles.Facial",id)

# @permission_required('Clientes.view_clientes') 
# def editarPagosSesionesCorporal(request,id):
#     mostrar=Sesiones.objects.filter(idSesiones=id).first()
#     contexto={"mostrar":mostrar}
#     return render(request,"Clientes/Editar-Pagos-Sesiones-Corporal.html",contexto)

# @permission_required('Clientes.view_clientes') 
# def cantidadClientes(request):
#     totalClientes = Clientes.objects.count().filter()
#     context= {"totalClientes":totalClientes}
#     return render(request,"partials/content.html", context)

# @permission_required('Clientes.view_clientes') 
# def actualizarPagosSesionesCorporal(request, id):
#     sesionesFecha=request.GET['fecha']
#     sesionesC=request.GET['secionesC']
#     sesionesValor=request.GET['valor']
#     sesionesAbono=request.GET['abono']

#     if sesionesAbono< sesionesValor:
#         actualizar=Sesiones.objects.get(idSesiones=id)
#         actualizar.fecha=sesionesFecha
#         actualizar.Nseciones=sesionesC
#         actualizar.valor=sesionesValor
#         actualizar.abono=sesionesAbono
#         actualizar.estado="Por pagar"
#         actualizar.save()
#     elif sesionesAbono> sesionesValor:
#         actualizar=Sesiones.objects.get(idSesiones=id)
#         actualizar.fecha=sesionesFecha
#         actualizar.Nseciones=sesionesC
#         actualizar.valor=sesionesValor
#         actualizar.abono=sesionesAbono
#         actualizar.estado="Devolver"
#         actualizar.save()
#     else:
#         actualizar=Sesiones.objects.get(idSesiones=id)
#         actualizar.fecha=sesionesFecha
#         actualizar.Nseciones=sesionesC
#         actualizar.valor=sesionesValor
#         actualizar.abono=sesionesAbono
#         actualizar.estado="Pagado"
#         actualizar.save()

