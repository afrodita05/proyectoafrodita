from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from Apps.Usuarios.models import User

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
    correo= request.POST['correo']
    nombreUsuario= request.POST['usuario']
    error= []
    errorCorreo= []
    errorUsuario= []
    if User.objects.filter(documento=documentoUsuario).exists():
        print("Error. El documento ingresado ya existe en otro usuario.")
        error.append(1)
        context={"error":error}
        return render(request, 'Usuarios/Crear-Usuario.html',context)
    else:
        print("Primer filtro completado")
        if User.objects.filter(email=correo).exists():
            
            errorCorreo.append(1)
            context={"errorCorreo":errorCorreo}
            return render(request, 'Usuarios/Crear-Usuario.html',context)
        else:
            print("Segundo filtro completado")
            if User.objects.filter(username=nombreUsuario).exists():
                errorUsuario.append(1)
                context={"errorUsuario":errorUsuario}
                return render(request, 'Usuarios/Crear-Usuario.html',context)
            else:
                print("Último filtro completado")
                nombrePersona= request.POST['nombre']
                password= request.POST['contrasena']
                usuarios=User(documento=documentoUsuario,nPersona=nombrePersona,username=nombreUsuario,password=make_password(password),email=correo)
                error.clear()
                errorUsuario.clear()
                errorCorreo.clear()
                usuarios.save()
                print("Documento: ",documentoUsuario,"Nombre: ",nombrePersona, "Usuario: ", nombreUsuario, "Contraseña: ", password, "Email: ", correo)
                return redirect("Usuario")

def editarU(request, id):
    mostrar=User.objects.filter(id=id).first()
    print(mostrar, "ID DEL USUARIO: ", id)
    print(mostrar.id, "PRUEBA 2")
    context={"mostrar":mostrar}
    return render(request,"Usuarios/Editar-Usuario.html",context)
    

def actualizarU(request, id):
    print("La id enviada es: ", id)
    errorUsuario= []
    errorCorreo= []
    errorContrasena= []
    
    nombrePersona= request.GET['nombre']
    nombreUsuario= request.GET['usuario']
    correo = request.GET['correo']
    password = request.GET['contrasena']
    password2 = request.GET['contrasena2']

    actualizar=User.objects.get(id=id)
    if (User.objects.filter(username=nombreUsuario).exists()) and (actualizar.username != nombreUsuario):
        
        errorUsuario.append(1)
        mostrar=User.objects.filter(id=id).first()
        context={"errorUsuario":errorUsuario, "mostrar":mostrar}
        return render(request,"Usuarios/Editar-Usuario.html",context)
        
    else:
        print("Primer filtro superado")
        if User.objects.filter(email=correo).exists() and (actualizar.email != correo):
            errorCorreo.append(1)
            mostrar=User.objects.filter(id=id).first()
            context={"errorCorreo":errorCorreo,"mostrar":mostrar}
            return render(request, 'Usuarios/Editar-Usuario.html',context)
        else:
            print("Segundo filtro superado")
            if password==password2:
                print("Tercer filtro superado")
                errorUsuario.clear()
                errorCorreo.clear()
                errorContrasena.clear()
                actualizar.nPersona=nombrePersona 
                actualizar.username=nombreUsuario 
                actualizar.email=correo
                actualizar.password=make_password(password)
                actualizar.save()
                return redirect("Usuario")
            else:
                errorContrasena.append(1)
                mostrar=User.objects.filter(id=id).first()
                context={"errorContrasena":errorContrasena, "mostrar":mostrar}
                return render(request, 'Usuarios/Editar-Usuario.html',context)

