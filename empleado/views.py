from django.shortcuts import render, HttpResponse

# Create your views here.
def empleados(request):
    return HttpResponse("Empleados")