import re
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from ConsoApp.models import Consolas, Distribuidores, Vendedores
from django.http import HttpResponse
from ConsoApp.forms import ConsolasForm, DistribuidoresForm, VendedoresForm
from typing import List
from django.http.request import QueryDict

# Create your views here.
def inicio(request):

      return render(request, "ConsoApp/inicio.html")

def distribuidores(request):

     return render(request, 'ConsoApp/distribuidores.html')

def consolas(request):

      return render(request, "ConsoApp/consolas.html")

def vendedores(request):

      return render(request, "ConsoApp/vendedores.html")

def busquedaConsola(request):

      return render(request, "ConsoApp/busquedaConsola.html")


def consolas(request):

      if request.method == 'POST':

            miFormulario = ConsolasForm(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  consolas = Consolas (nombre=informacion['nombre'], modelo=informacion['modelo'], stock=informacion['stock'])

                  consolas.save()

                  return render(request, "ConsoApp/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario = ConsolasForm() #Formulario vacio para construir el html

      return render(request, "ConsoApp/consolas.html", {"miFormulario":miFormulario})




def vendedores(request):

      if request.method == 'POST':

            miFormulario = VendedoresForm(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  vendedores = Vendedores (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 

                  vendedores.save()

                  return render(request, "ConsoApp/vendedores.html")

      else: 

            miFormulario= VendedoresForm() 

      return render(request, "ConsoApp/vendedores.html", {"miFormulario":miFormulario})

def distribuidores(request):

      if request.method == 'POST':

            miFormulario = DistribuidoresForm(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  distribuidores = Distribuidores (empresa=informacion['empresa'], ingreso=informacion['ingreso']) 

                  distribuidores.save()

                  return render(request, "ConsoApp/distribuidores.html")

      else: 

            miFormulario= DistribuidoresForm()

      return render(request, "ConsoApp/distribuidores.html", {"miFormulario":miFormulario})

def buscar(request):
      if request.GET["nombre"]:
            nombre = request.GET['nombre']
            consolas = Consolas.objects.filter(nombre__icontains=nombre)
            return render(request, "ConsoApp/inicio.html", {"consolas":consolas, "nombre":nombre})
      else:
            respuesta = "No enviaste datos"

      return render(request, 'ConsoApp/busquedaConsola.html', {'respuesta':respuesta})