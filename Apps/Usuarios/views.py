from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView
from Apps.Usuarios.models import Usuarios

# Create your views here.

# class Usuarioview(TemplateView):
#     pass

# Usuarios = Usuarioview.as_view(
#     template_name="Usuarios/Usuarios.html"
# )
# def formularioUsuarios(request):
#     return render(request,"Usuarios/Usuarios.html",Usuarios)

# Crear_Usuario = Usuarioview.as_view(
#     template_name="Usuarios/Crear-Usuario.html"
# )
# Editar_Usuario = Usuarioview.as_view(
#     template_name="Usuarios/Editar-Usuario.html"
# )


def usuario(request):
    usuario=Usuarios.objects.filter()
    context={"usuario":usuario}
    return render(request,"Usuarios/Usuarios.html",context)


def formularioUsuario(request):
    return render(request,'Usuarios/Crear-Usuario.html')


def crearUsuario(request):
    documentoUsuario= request.POST['documento']
    nombrePersona= request.POST['nombre']
    nombreUsuario= request.POST['usuario']
    password= request.POST['contrasena']
    correo= request.POST['correo']
    usuarios=Usuarios(documento=documentoUsuario,nPersona=nombrePersona,nUsuario=nombreUsuario,contrasena=password,correo=correo)
    usuarios.save()
    return redirect("Usuario")


def editarU(request, id):
    mostrar=Usuarios.objects.filter(idUsuario=id).first()
    context={"mostrar":mostrar}
    return render(request,"Usuarios/Editar-Usuario.html",context)
    

def actualizarU(request, id):

    nombrePersona= request.GET['nombre']
    nombreUsuario= request.GET['usuario']
    correo = request.GET['correo']
    password = request.GET['contrasena']
    
    actualizar=Usuarios.objects.get(idUsuario=id)
    actualizar.nPersona=nombrePersona #Será este?
    actualizar.nUsuario=nombreUsuario 
    actualizar.correo=correo
    actualizar.contrasena=password
    actualizar.save()
    return redirect("/usuario/")