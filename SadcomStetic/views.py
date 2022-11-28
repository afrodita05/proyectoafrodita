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

        clientes = Clientes.objects.filter()
        todasCitas = Citas.objects.filter()
        clientesConCitas = Citas.objects.values_list('idCliente').distinct()
        print("ESTO ES: ", clientesConCitas)
        for clientes.idCliente in clientesConCitas:
            print("EL ID ES SEÑOR JESUCRISTO TE LO RUEGO:", clientesConCitas)
            idClientesEnCitas = clientes.idCliente
        
            citaActual = Citas.objects.filter(idCliente=idClientesEnCitas)
            

            citasMostrar = list(citaActual)
            print(citaActual)
            print("La lista es: ", citasMostrar)
            
            

        # insumosServicio = Citas.objects.filter(idServicio_id=idServicio).values_list('idInsumo', flat= True)
        context={"compraC":compraC, "insumoC":insumoC,"proveedorC":proveedorC,"clienteC":clienteC,"citasMostrar":citasMostrar}
        return render(request, "dashboard.html", context)
    
    



class Settings(View):
    template_name = "settings.html"

    def __init__(self, *args):
        super(Settings, self).__init__(*args)

    def get(self, request):
        k = TOTPDevice.objects.filter(user=request.user)
        context_data = {"k": k}
        return render(request, self.template_name, context_data)
