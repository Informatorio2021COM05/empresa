from django.db import models
from departamento.models import Departamento
# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50, null=True)
    nacimiento = models.DateField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey(Departamento,
        on_delete=models.SET_NULL,
        null=True)
