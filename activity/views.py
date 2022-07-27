from django.shortcuts import render
from activity.models import Caja, Distribuidores
from .forms import CajaForm, DistribuidoresForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def work_employee(request):
      if request.method == 'POST':

            miFormulario = CajaForm(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                caja = Caja (entrada=informacion['entrada'], salida=informacion['salida'], motivo=informacion['motivo']) 
                caja.save()
                return render(request, "activity/work_employee.html")
      else: 

            miFormulario = CajaForm() 
      return render(request, "activity/work_employee.html", {"miFormulario":miFormulario})
  

def distribuidores(request):

      return render(request, "activity/distribuidores.html")

def work_admin(request):

      return render(request, "activity/work_admin.html")


def distribuidores_registro(request):

      if request.method == 'POST':

            miFormulario = DistribuidoresForm(request.POST)

            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  distribuidores = Distribuidores (empresa=informacion['empresa']) 
                  distribuidores.save()
                  return render(request, "activity/distribuidores_registro.html")
      else: 

            miFormulario= DistribuidoresForm()
      return render(request, "activity/distribuidores_registro.html", {"miFormulario":miFormulario})
  
class DistribuidoresList(LoginRequiredMixin, ListView):

      model = Distribuidores
      template_name = "Activity/distribuidores_list.html"



class DistribuidoresDetalle(DetailView):

      model = Distribuidores
      template_name = "activity/distribuidores_detalle.html"



class DistribuidoresCreacion(CreateView):

      model = Distribuidores
      success_url = "/activity/distribuidores/list"
      fields = ['empresa']


class DistribuidoresUpdate(UpdateView):

      model = Distribuidores
      success_url = "/activity/distribuidores/list"
      fields  = ['empresa']


class DistribuidoresDelete(DeleteView):

      model = Distribuidores
      success_url = "/activity/distribuidores/list"
