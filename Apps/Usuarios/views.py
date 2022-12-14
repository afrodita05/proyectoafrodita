from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from Apps.Usuarios.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required

#@login_required
@permission_required('Usuarios.view_user',raise_exception=True)
def usuario(request):
    usuario=User.objects.all()
    # usuario = {group.name: group.user_set.values_list('id', flat=True) for group in Group.objects.all()}
    context={"usuario":usuario}
    return render(request,"Usuarios/Usuarios.html",context)

@permission_required('Usuarios.view_user',raise_exception=True) 
def formularioUsuario(request):
    rol=Group.objects.filter()
    context={"rol":rol}
    return render(request,'Usuarios/Crear-Usuario.html',context)

@permission_required('Usuarios.view_user',raise_exception=True) 
def crearUsuario(request):
    documentoUsuario= request.POST['documento']
    correo= request.POST['correo']
    nombreUsuario= request.POST['usuario']
    rol = request.POST['rol']
    fotop = request.FILES['fotop']
    error= []
    errorCorreo= []
    errorUsuario= []
    if User.objects.filter(documento=documentoUsuario).exists():
       
        error.append(1)
        context={"error":error}
        return render(request, 'Usuarios/Crear-Usuario.html',context)
    else:
        
        if User.objects.filter(email=correo).exists():
            
            errorCorreo.append(1)
            context={"errorCorreo":errorCorreo}
            return render(request, 'Usuarios/Crear-Usuario.html',context)
        else:
            
            if User.objects.filter(username=nombreUsuario).exists():
                errorUsuario.append(1)
                context={"errorUsuario":errorUsuario}
                return render(request, 'Usuarios/Crear-Usuario.html',context)
            else:
                
                nombrePersona= request.POST['nombre']
                password= request.POST['contrasena']
                usuarios=User(documento=documentoUsuario,nPersona=nombrePersona,username=nombreUsuario,password=make_password(password),email=correo,foto=fotop)
                error.clear()
                errorUsuario.clear()
                errorCorreo.clear()
                usuarios.save()
                
                usuarios.groups.add(rol)


                return redirect("Usuario")

@permission_required('Usuarios.view_user',raise_exception=True) 
def editarU(request, id):
    rol=Group.objects.filter()
    mostrar=User.objects.filter(id=id).first()
   
    context={"mostrar":mostrar, "rol": rol}
    return render(request,"Usuarios/Editar-Usuario.html",context)
    

@permission_required('Usuarios.view_user',raise_exception=True) 
def actualizarU(request, id):
    
    errorUsuario= []
    errorCorreo= []
    errorContrasena= []
    
    nombrePersona= request.POST['nombre']
    nombreUsuario= request.POST['usuario']
    correo = request.POST['correo']
    password = request.POST['contrasena']
    password2 = request.POST['contrasena2']
    fotop = request.FILES['fotop']
    rol= request.POST['rol']
    actualizar=User.objects.get(id=id)
    if (User.objects.filter(username=nombreUsuario).exists()) and (actualizar.username != nombreUsuario):
        
        errorUsuario.append(1)
        mostrar=User.objects.filter(id=id).first()
        context={"errorUsuario":errorUsuario, "mostrar":mostrar}
        return render(request,"Usuarios/Editar-Usuario.html",context)
        
    else:
        
        if User.objects.filter(email=correo).exists() and (actualizar.email != correo):
            errorCorreo.append(1)
            mostrar=User.objects.filter(id=id).first()
            context={"errorCorreo":errorCorreo,"mostrar":mostrar}
            return render(request, 'Usuarios/Editar-Usuario.html',context)
        else:
            
            if password==password2:
               
                errorUsuario.clear()
                errorCorreo.clear()
                errorContrasena.clear()
                actualizar.nPersona=nombrePersona 
                actualizar.username=nombreUsuario 
                actualizar.email=correo
                actualizar.password=make_password(password)
                actualizar.foto=fotop
                actualizar.save()

                users_in_group = Group.objects.get(id=rol).user_set.all()
                if actualizar in users_in_group:
                    return redirect("Usuario")
                else:
                    actualizar.groups.add(rol)
                    return redirect("Usuario")
            else:
                errorContrasena.append(1)
                mostrar=User.objects.filter(id=id).first()
                context={"errorContrasena":errorContrasena, "mostrar":mostrar}
                return render(request, 'Usuarios/Editar-Usuario.html',context)

