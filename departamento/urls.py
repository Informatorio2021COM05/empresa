from django.urls import path
from . import views

app_name = "departamento"
urlpatterns = [
    path("hola_mundo/", views.hola_mundo, name="hola_mundo"),

    path("", views.departamentos, name="departamentos"),
    path("<int:id>/", views.ver_departamento, name="ver_departamento"),
    #nuevo
    path("nuevo/", views.nuevo_dpto, name="nuevo_dpto"),
    path("<int:id>/editar/", views.editar_departamento, name="editar_departamento"),
    #editar departamettno
]
