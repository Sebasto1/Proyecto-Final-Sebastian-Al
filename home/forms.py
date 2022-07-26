from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dataclasses import fields

class AdministradorForm(forms.Form):
    nombre = forms.CharField(max_length=(20))
    modelo = forms.CharField(max_length=(20))
    email = forms.EmailField()

class EmpleadosForm(forms.Form):
    nombre = forms.CharField(max_length=(20))
    apellido = forms.CharField(max_length=(20))
    email = forms.EmailField()

class DistribuidoresForm(forms.Form):
    nombre = forms.CharField(max_length=(20))
    ingreso = forms.IntegerField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    firt_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
        
class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
        
class CajaForm(forms.Form):
    ingreso = forms.IntegerField()
    salida = forms.IntegerField()
    