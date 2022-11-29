from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from allauth.account.views import PasswordSetView, PasswordChangeView
from django_otp.plugins.otp_totp.models import TOTPDevice
from Apps.Compras.models import *
from Apps.Insumos.models import *
from Apps.Clientes.models import *
from Apps.Proveedores.models import *
from Apps.Citas.models import *
from django.db import connection


# Dashboard
@login_required
def index(request):

    return render(request,'partials/base.html')

class DashboardView(View):
    
    def get(self, request):
        insumoC=Insumo.objects.filter().count
        compraC=Compra.objects.filter().count
        proveedorC=Proveedor.objects.filter().count
        clienteC=Clientes.objects.filter().count
        citasMostrar= " "
        clientes = Clientes.objects.filter()
        todasCitas = Citas.objects.filter()
        clientesConCitas = Citas.objects.values_list('idCliente').distinct().values('idCliente')
        print("ESTO ES: ", clientesConCitas)
        print(clientesConCitas,)
        serviciosCliente=[]
        cursor= []
        
        for clientes.idCliente in clientesConCitas:
            print("EL ID ES SEÑOR JESUCRISTO TE LO RUEGO:", clientesConCitas)
            idClientesEnCitas = clientes.idCliente

            citaActual = Citas.objects.filter(idCliente__in=clientesConCitas).distinct()
            print("Clientesconcitas es: ",clientesConCitas)
            print("Los clientes tipo son: ",type(clientes))
            print("El tipo de cita actual es: ", type(citaActual))
            print("Los valores de cita actual son: ", citaActual)


            totalServicios= Citas.objects.filter(idCliente__in=clientesConCitas).values_list('idServicio', flat= True)
            print(totalServicios, "ESSSS")
            #reversar valores de citactual para buscar servicios asociados a ellos, agregar servicios a lista, sacar longitud de lista, imprimir en el context
            cantidadServicios= 120

        with connection.cursor() as cursor:
            cursor.execute('''SELECT nombre, documento, COUNT(idServicio_id) AS totalServicios 
            FROM afrodita.citas_citas AS A
            INNER JOIN clientes_clientes AS B
            ON A.idCliente_id = B.idCliente 
            GROUP BY idCliente_id''')
            rows = cursor.fetchall()
            rows = list(rows)
            print("El row es: ",rows)
            for cliente in citaActual:
                print(cliente.idCliente.idCliente)

            
        context={"compraC":compraC, "insumoC":insumoC,"proveedorC":proveedorC,"clienteC":clienteC,"citaActual":citaActual, "cantidadServicios":cantidadServicios, "cursor":rows}
        return render(request, "dashboard.html", context)
    
    



class Settings(View):
    template_name = "settings.html"

    def __init__(self, *args):
        super(Settings, self).__init__(*args)

    def get(self, request):
        k = TOTPDevice.objects.filter(user=request.user)
        context_data = {"k": k}
        return render(request, self.template_name, context_data)
