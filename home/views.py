import re
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from home.models import Distribuidores, Caja
from django.http import HttpResponse
from home.forms import CajaForm
from typing import List
from django.http.request import QueryDict

# Create your views here.
def home(request):

      return render(request, "home/home.html")


def caja(request):
      if request.method == 'POST':

            miFormulario = CajaForm(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  caja = caja(ingreso=informacion['ingreso'], salida=informacion['salida'], fecha=informacion['fecha']) 

                  caja.save()

                  return render(request, "home/caja.html")

      else: 

            miFormulario = CajaForm() 

      return render(request, "home/caja.html", {"miFormulario":miFormulario})