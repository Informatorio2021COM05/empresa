from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return "departamento: " + self.nombre