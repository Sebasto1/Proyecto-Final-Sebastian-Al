from unicodedata import name
from django.shortcuts import render, redirect

from users.models import User
from .forms import UpdateUserForm, UpdateProfileForm,UpdateProfileForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group

from django.views import View
from django.http import HttpResponse
from django.http.request import QueryDict
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def register(request):
      return render(request, "users/register.html")

def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
               
                  user = authenticate(username = username , password = password)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "home/home.html", {"mensaje": f"Bienvenido/a {username}"})
                  else:
                       
                        return render (request, "home/home.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "home/home.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "users/login.html", {'form': form})

class RegisterViewEmployee(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register_employee.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect('home/home')

        return render(request, self.template_name, {'form': form})

class RegisterViewAdmin(View):
      form_class = RegisterForm
      initial = {'key': 'value'}
      template_name = 'users/register_admin.html'

      def get(self, request, *args, **kwargs):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

      def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)

            if form.is_valid():
                  form.save()

                  username = form.cleaned_data.get('username')
                  messages.success(request, f'Cuenta creada para {username}')

                  return redirect('home/home')

            return render(request, self.template_name, {'form': form})

def logout_request(request):
       logout(request)
       messages.info(request, "Saliste sin problemas")
       return redirect("home/home.html")
 
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil se actualizo correctamente')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "Le enviamos un Email para resetear su contraseña, " \
                      "Si existe una cuenta con el mail ingresado le llegara en unos minutos." \
                      "Si no recibe un email, por favor revisar su carpeta de spam"
    success_url = reverse_lazy('home/home')

