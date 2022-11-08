from django.urls import path  
from . import views

urlpatterns =[
    path ('editarInsumo/', views.editarInsumo, ),
    path ('edicionInsumos/<int:idInsumo>', views.edicionInsumos, name= 'editar' ),
    
] 