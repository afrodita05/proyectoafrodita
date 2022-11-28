from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from allauth.account.views import PasswordSetView, PasswordChangeView
from django_otp.plugins.otp_totp.models import TOTPDevice
from Apps.Compras.models import Compra
from Apps.Insumos.models import Insumo
from Apps.Clientes.models import Clientes
from Apps.Proveedores.models import Proveedor



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
        context={"compraC":compraC, "insumoC":insumoC,"proveedorC":proveedorC,"clienteC":clienteC}
        return render(request, "dashboard.html", context)
    
    



class Settings(View):
    template_name = "settings.html"

    def __init__(self, *args):
        super(Settings, self).__init__(*args)

    def get(self, request):
        k = TOTPDevice.objects.filter(user=request.user)
        context_data = {"k": k}
        return render(request, self.template_name, context_data)
