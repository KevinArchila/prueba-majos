from .models import Cargo_usuarios

def cargos(request):
    cargos = Cargo_usuarios.objects.all()
    return {'cargos': cargos}


