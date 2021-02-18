from django.contrib import admin

from .models import Empleado
# Register your models here.

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "apellido",
        "departamento"
    ]

#admin.site.register(Empleado, EmpleadoAdmin)