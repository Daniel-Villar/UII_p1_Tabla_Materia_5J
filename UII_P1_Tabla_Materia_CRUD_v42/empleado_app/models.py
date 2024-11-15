from django.db import models

# Create your models here.
class Empleados(models.Model):
    idEmpleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    Edad=models.PositiveSmallIntegerField()
    sexo=models.CharField(max_length=100)
    no_telefono=models.PositiveSmallIntegerField()
    Direccion=models.CharField(max_length=100)
    Forma_pago=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
