from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from Apps.Usuarios.models import Usuarios, User

#@login_required
def usuario(request):
    usuario=User.objects.filter()
    context={"usuario":usuario}
    return render(request,"Usuarios/Usuarios.html",context)

def pruebaCr(request):
    usuario = User.objects.create_user('pepe', 'pepe@pepe.com', 'pepelo')
    usuario.save()
    return redirect("Usuario")

def formularioUsuario(request):
    return render(request,'Usuarios/Crear-Usuario.html')


def crearUsuario(request):
    documentoUsuario= request.POST['documento']
    error= []
    if User.objects.filter(documento=documentoUsuario).exists():
        print("Error. El documento ingresado ya existe en otro usuario.")
        error.append(1)
        context={"error":error}
        return render(request, 'Usuarios/Crear-Usuario.html',context)
    else:
        nombrePersona= request.POST['nombre']
        nombreUsuario= request.POST['usuario']
        password= request.POST['contrasena']
        correo= request.POST['correo']
        usuarios=User(documento=documentoUsuario,nPersona=nombrePersona,username=nombreUsuario,password=make_password(password),email=correo)
        error.clear()
        usuarios.save()

    
    return redirect("Usuario")


def editarU(request, id):
    mostrar=User.objects.filter(id=id).first()
    context={"mostrar":mostrar}
    return render(request,"Usuarios/Editar-Usuario.html",context)
    

def actualizarU(request, id):

    nombrePersona= request.GET['nombre']
    nombreUsuario= request.GET['usuario']
    correo = request.GET['correo']
    password = request.GET['contrasena']
    
    actualizar=User.objects.get(id=id)
    actualizar.nPersona=nombrePersona #Será este?
    actualizar.username=nombreUsuario 
    actualizar.email=correo
    actualizar.password=make_password(password)
    actualizar.save()
    return redirect("Usuario")

    
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
