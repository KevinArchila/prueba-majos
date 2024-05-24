from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario_servicio, Cargo_usuarios, Usuarios
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.


def inicio_servicio(request):

    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre')
        contra = request.POST.get('contra')
        usuario = Usuario_servicio.objects.filter(nombre=nombre_usuario, contraseña = contra).first()
        if usuario is not None:
            request.session['usuario_id'] = usuario.id
            request.session['nombre_usuario'] = usuario.nombre
            return redirect("perfiles")
        else:
            return render(request, "login_usuario.html", {'mensaje': "Usuario o contraseña invalido", 
                                                            "campo_password": contra, "campo_name": nombre_usuario})
    else:
        return render(request, "login_usuario.html")



def otra_vista(request):
    usuario_id = request.session.get('usuario_id')
    nombre_usuario = request.session.get('nombre_usuario')
    if usuario_id and nombre_usuario:
        return render(request, "prueba.html", {'id': usuario_id, 'nombre': nombre_usuario})
    else:
        return redirect("hola")
    
def cerrar(request):

    logout(request)
    return redirect("hola")


def registro_perfil(request):
    if request.method == "POST":
        cargo_select = request.POST.get("cargo")
        nombre_perfil = request.POST.get("nombre")
        password = request.POST.get("password")
        repetir_password = request.POST.get("repetir_password")

        if password == repetir_password:
            if len(nombre_perfil) < 20:
                if cargo_select != "":
                    cargo = Cargo_usuarios.objects.get(nombre_cargo = cargo_select)
                    perfil = Usuarios(nombre=nombre_perfil, contraseña = password, cargo = cargo, estado = "True")
                    perfil.save()
                    return redirect("perfiles")
                else:
                    return render(request, "registro_perfil.html", {"mensaje_cargo": "el cargo no fue seleccionado"})
            else:
                return render(request, "registro_perfil.html", {"mensaje_name": "el perfil no puede superar los 20 caracteres"})
        else:
            return render(request, "registro_perfil.html", {"mensaje_password": "las contraseñas no son iguales"})
    else:
        cargos = Cargo_usuarios.objects.all()
        return render(request, "registro_perfil.html")

def perfiles_usuarios(request):
    id_usuario_servicio = request.session.get("usuario_id")
    if id_usuario_servicio:
        usuario_servicio_id = request.session.get("usuario_id")
        perfiles = Usuarios.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
        print(perfiles)
        return render(request, "perfiles.html", {"perfiles": perfiles})
    else:
        return redirect("Servicio")

def login_perfil(request, perfil_id):
    if request.method == "POST":
        password_perfil = request.POST.get("password_perfil")
        perfil = Usuarios.objects.filter(id=perfil_id, contraseña=password_perfil).first()
        if perfil is not None:
            request.session["name_perfil"] = perfil.nombre
            request.session["cargo_perfil"] = perfil.cargo.id
            request.session["id_perfil"] = perfil.id          
            return redirect("inicio")
        else:
            perfil = Usuarios.objects.get(id=perfil_id)
            return render(request, "login_perfil.html", {"perfil": perfil, "mensaje": "contraseña invalida"})

    perfil = Usuarios.objects.get(id=perfil_id)
    return render(request, "login_perfil.html", {"perfil": perfil})

def log_out_servicio(request):
    request.session["usuario_id"] = None
    return redirect("Servicio")
    


