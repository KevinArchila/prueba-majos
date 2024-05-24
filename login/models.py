from django.db import models

# Create your models here.
class Usuario_servicio(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(max_length=250, unique=True)
    contraseña = models.CharField(max_length=12)
    estado = models.CharField(max_length=6)

class Cargo_usuarios(models.Model):
    nombre_cargo = models.CharField(max_length=25)
    permiso = models.CharField(max_length=10)
    estado = models.CharField(max_length=7)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)


class Usuarios(models.Model):
    cargo = models.ForeignKey(Cargo_usuarios, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=12)
    estado = models.CharField(max_length=6)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)


