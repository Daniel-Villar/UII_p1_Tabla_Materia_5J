from django.shortcuts import render
from .models import Materia
# Create your views here.
def inicio_vista(request):
    lasmateria=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias":lasmateria})