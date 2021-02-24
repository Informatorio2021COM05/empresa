from django.shortcuts import render, HttpResponse
from .models import Empleado
# Create your views here.
def empleados(request):
    lista_empleados = Empleado.objects.all()
    return render(request, "empleado/empleados.html",{"lista_empleados":lista_empleados})
