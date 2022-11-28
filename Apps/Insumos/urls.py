from django.urls import path  
from . import views

urlpatterns =[
    path ('editarInsumo/<int:id>', views.editarInsumo, name= 'actualizarI' ),
    path ('edicionInsumos/<int:id>', views.edicionInsumos, name= 'editar' ),
    
] 