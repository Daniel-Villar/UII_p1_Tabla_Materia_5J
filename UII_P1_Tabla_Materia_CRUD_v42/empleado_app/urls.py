from django.urls import path
from empleado_app import views

urlpatterns = [
    path("",views.inicio_vista, name="inicio_vista"),
    path("registrarEmpleados/", views.registrarEmpleados, name="registrarEmpleados"),
    path("seleccionarEmpleados/<codigo>",views.seleccionarEmpleados, name="seleccionarEmpleados"),
    path("editarEmpleados/", views.editarEmpleados, name="editarEmpleados"),
    path("borrarEmpleados/<codigo>",views.borrarEmpleados, name="borrarEmpleados"),
]
