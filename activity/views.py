from django.shortcuts import render
from activity.models import Caja, Distribuidores
from .forms import CajaForm, DistribuidoresForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def caja(request):
      if request.method == 'POST':

            miFormulario = CajaForm(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:
                

                informacion = miFormulario.cleaned_data

                caja = Caja (entrada=informacion['entrada'], salida=informacion['salida'], motivo=informacion['motivo']) 
                caja.save()

                return render(request, "activity/caja.html")

      else: 

            miFormulario = CajaForm() 

      return render(request, "activity/caja.html", {"miFormulario":miFormulario})
  
  
def distribuidores(request):

      return render(request, "activity/distribuidores.html")


def distribuidor(request):

      if request.method == 'POST':

            miFormulario = AdministradorForm(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  administrador = Administrador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

                  administrador.save()

                  return render(request, "ConsoApp/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario = AdministradorForm() #Formulario vacio para construir el html

      return render(request, "accounts/administrador.html", {"miFormulario":miFormulario})
  
class DistribuidoresList(LoginRequiredMixin, ListView):

      model = Distribuidores
      template_name = "Activity/distribuidores_list.html"



class DistribuidoresDetalle(DetailView):

      model = Distribuidores
      template_name = "Activity/distribuidores_detalle.html"



class DistribuidoresCreacion(CreateView):

      model = Distribuidores
      success_url = "/Activity/Distribuidores/list"
      fields = ['nombre', 'camada']


class DistribuidoresUpdate(UpdateView):

      model = Distribuidores
      success_url = "/Activity/Distribuidores/list"
      fields  = ['empresa']


class DistribuidoresDelete(DeleteView):

      model = Distribuidores
      success_url = "/Activity/Distribuidores/list"
