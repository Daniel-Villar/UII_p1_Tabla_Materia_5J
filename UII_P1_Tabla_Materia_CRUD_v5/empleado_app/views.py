from django.shortcuts import render,redirect
from .models import Empleados

# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados=Empleados.objects.all()
    return render(request,"gestionarempleado.html",{"losempleados2":losempleados})

def registrarEmpleados(request):
    idEmpleado=request.POST["txtidEmpleado"]
    nombre=request.POST["txtnombre"]
    Fecha_nac=request.POST["txtFecha-nac"]
    sexo=request.POST["txtSexo"]
    email=request.POST["txtEmail"]
    no_telefono=request.POST["txtTelefono"]
    puesto=request.POST["txtPuesto"]

    guardarEmpleados=Empleados.objects.create(
        idEmpleado=idEmpleado,
        nombre=nombre,
        Fecha_nac=Fecha_nac,
        sexo=sexo,
        no_telefono=no_telefono,
        email=email,
        puesto=puesto
    ) # Guarda el Registro

    return redirect("Empleado")

def seleccionarEmpleados(request,idEmpleado):
    empleado=Empleados.objects.get(idEmpleado=idEmpleado)
    return render(request,"editarempleado.html",{"losempleados":empleado})

def editarEmpleados(request):
    idEmpleado=request.POST["txtidEmpleado"]
    nombre=request.POST["txtnombre"]
    Fecha_nac=request.POST["txtFecha-nac"]
    sexo=request.POST["txtSexo"]
    email=request.POST["txtEmail"]
    no_telefono=request.POST["txtTelefono"]
    puesto=request.POST["txtPuesto"]
    empleado=Empleados.objects.get(idEmpleado=idEmpleado)
    empleado.nombre=nombre
    empleado.Fecha_nac=Fecha_nac
    empleado.sexo=sexo
    empleado.email
    empleado.no_telefono=no_telefono
    empleado.puesto=puesto
    empleado.save() #Guarda Registro Actualizado
    return redirect("Empleado")

def borrarEmpleados(request,idEmpleado):
    empleado=Empleados.objects.get(idEmpleado=idEmpleado)
    empleado.delete() #Borra el Registro
    return redirect("Empleado")