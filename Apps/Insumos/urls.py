from django.urls import path  
from . import views

urlpatterns =[
    path ('crearInsumos/', views.crearInsumos),
    path ('eliminarInsumos/<idInsumos>', views.eliminarInsumos),
    path ('editarInsumo/', views.editarInsumo, ),
    path ('edicionInsumos/<int:idInsumos>', views.edicionInsumos, name= 'editar' ),
    
] 