from django.db import models

# Create your models here.
class Empleados(models.Model):
    idEmpleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    Fecha_nac=models.PositiveSmallIntegerField()
    sexo=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    no_telefono=models.PositiveSmallIntegerField()
    puesto=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
