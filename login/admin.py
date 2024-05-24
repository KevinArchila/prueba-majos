from django.contrib import admin
from .models import Usuarios, Usuario_servicio, Cargo_usuarios
# Register your models here.

admin.site.register(Usuario_servicio)
admin.site.register(Usuarios)
admin.site.register(Cargo_usuarios)
