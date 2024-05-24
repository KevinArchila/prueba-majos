from django.urls import path
from . import views

urlpatterns = [
    path('inicio_servicio/', views.inicio_servicio, name="Servicio"),
    path('prueba/', views.otra_vista, name="perfiles"),
    path('cerrar/', views.cerrar, name="cerrar"),
    path('perfiles/', views.perfiles_usuarios, name="perfiles"),
    path('login_perfil/<perfil_id>', views.login_perfil, name="login_perfil"),
    path('log_out_servicio/', views.log_out_servicio, name="log_out_servicio"),
]
