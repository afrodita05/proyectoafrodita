from dataclasses import field
from django import forms
from .models import Insumo

class InsumoForm(forms.Form):
    class meta:
        model = Insumo
        fields = '__all__'