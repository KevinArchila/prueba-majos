from django.shortcuts import render, redirect
from login.models import Cargo_usuarios

# Create your views here.

def cerrar_sesion(request):
    request.session["name_perfil"] = None
    request.session["id_perfil"] = None
    request.session["cargo_perfil"] = None
    return redirect("perfiles")


def home(request):
    request.session["permiso_parametro"] = False
    inicio = "inicio"
    nombre = request.session.get("name_perfil")
    id_perfil = request.session.get("id_perfil")
    cargo_perfil = request.session.get("cargo_perfil")
    permisos = Cargo_usuarios.objects.filter(id=cargo_perfil).first()
    if nombre and id_perfil:
        inicio = "inicio"
        return render(request, "home.html", {"nombre": nombre, "id": id_perfil, "cargos": permisos, "inicio": inicio})
    else:
        return redirect("perfiles")