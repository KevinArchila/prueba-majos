from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('cerrar_sesion_perfil/', views.cerrar_sesion, name="cerrar_sesion_perfil"), 
]
