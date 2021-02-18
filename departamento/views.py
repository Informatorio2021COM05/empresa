from django.shortcuts import render, HttpResponse, Http404, get_object_or_404,redirect
from .models import Departamento
from .forms import DepartamentoForm
# Create your views here.
def hola_mundo(request):
    #return HttpResponse("Hola Mundo")
    template = "departamento/hola_mundo.html"
    contexto = {
        "nombre":"Pedro",
        "numero":1234
    }
    return render(request, template, contexto)

def departamentos(request):
    departamentos = Departamento.objects.all()

    template = "departamento/departamentos.html"
    contexto = {
        "lista_dptos":departamentos,
    }
    return render(request, template, contexto)


def ver_departamento(request, id):
    try:
        dpto = Departamento.objects.get(pk=id)
    except Departamento.DoesNotExist:
        raise Http404("no se encontró")

    #dpto = get_object_or_404(Departamento, pk=id)

    #dpto.empleado_set.all()
    template = "departamento/departamento.html"
    contexto = {
        "dpto":dpto,
    }
    return render(request, template, contexto)

def nuevo_dpto(request):
    print(request.POST)
    
    form = DepartamentoForm()
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            dpto = form.save()
            return redirect("departamento:ver_departamento", dpto.id)


    contexto = {"form":form}
    template = "departamento/nuevo.html"
    return render(request, template, contexto)

def editar_departamento(request,id):
    try:
        dpto = Departamento.objects.get(pk=id)
    except Departamento.DoesNotExist:
        raise Http404("no se encontró")

    if request.method == "GET":
        form = DepartamentoForm(instance=dpto)

    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=dpto)
        if form.is_valid():
            dpto = form.save()
            return redirect("departamento:ver_departamento", dpto.id)    


    template = "departamento/nuevo.html"
    contexto = {"form":form}
    return render(request, template, contexto)