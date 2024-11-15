from django.shortcuts import render,redirect
from .models import Empleados

# Create your views here.
def inicio_vista(request):
    losempleados=Empleados.objects.all()
    return render(request,"gestionarempleado.html",{"losempleados":losempleados})

def registrarEmpleados(request):
    idEmpleado=request.POST["txtidEmpleado"]
    nombre=request.POST["txtnombre"]
    Edad=request.POST["txtEdad"]
    sexo=request.POST["txtSexo"]
    no_telefono=request.POST["txtTelefono"]
    Direccion=request.POST["txtDireccion"]
    Forma_pago=request.POST["txtPago"]


    guardarEmpleados=Empleados.objects.create(
        idEmpleado=idEmpleado,
        nombre=nombre,
        Edad=Edad,
        sexo=sexo,
        no_telefono=no_telefono,
        Direccion=Direccion,
        Forma_pago=Forma_pago
    ) # Guarda el Registro

    return redirect("/")

def seleccionarEmpleados(request,idEmpleado):
    empleado=Empleados.objects.get(idEmpleado=idEmpleado)
    return render(request,"editarempleado.html",{"losempleados":empleado})

def editarEmpleados(request):
    idEmpleado=request.POST["txtidEmpleado"]
    nombre=request.POST["txtnombre"]
    Edad=request.POST["txtEdad"]
    sexo=request.POST["txtSexo"]
    no_telefono=request.POST["txtTelefono"]
    Direccion=request.POST["txtDireccion"]
    Forma_pago=request.POST["txtPago"]
    empleado=Empleados.objects.get(idEmpleado=idEmpleado)
    empleado.nombre=nombre
    empleado.Edad=Edad
    empleado.sexo=sexo
    empleado.no_telefono=no_telefono
    empleado.Direccion=Direccion
    empleado.Forma_pago=Forma_pago
    empleado.save() #Guarda Registro Actualizado
    return redirect("/")

def borrarEmpleados(request,idEmpleado):
    empleado=Empleados.objects.get(idEmpleado=idEmpleado)
    empleado.delete() #Borra el Registro
    return redirect("/")