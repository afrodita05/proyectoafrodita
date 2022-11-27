from django.urls import path  
from . import views

urlpatterns =[
    path ('editarInsumo/<int:idInsumo>', views.editarInsumo, name= 'actualizarI' ),
    path ('edicionInsumos/<int:idInsumo>', views.edicionInsumos, name= 'editar' ),
    
] 