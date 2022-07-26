from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, User
from dataclasses import fields


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100,required=True, widget=forms.TextInput())
    username = forms.CharField(max_length=100,required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True,widget=forms.TextInput())
    password1 = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput())
    password = forms.CharField(max_length=50,required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')
        

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
