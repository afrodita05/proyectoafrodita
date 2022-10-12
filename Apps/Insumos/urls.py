from django.urls import path  
from . import views

urlpatterns =[
    path ('crearInsumos/', views.crearInsumos),
    path ('eliminarInsumos/<idInsumo>', views.eliminarInsumos),
    path ('editarInsumo/', views.editarInsumo, ),
    path ('edicionInsumos/<int:idInsumo>', views.edicionInsumos, name= 'editar' ),
    
] 