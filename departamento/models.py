from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return "departamento: " + self.nombre

    def sueldo_total(self):

        empleados = self.empleado_set.all()
        total = 0
        for emp in empleados:
            total += emp.sueldo
        return total