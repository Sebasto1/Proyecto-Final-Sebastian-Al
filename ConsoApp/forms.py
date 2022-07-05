from django import forms

class ConsolasForm(forms.Form):
    nombre = forms.CharField(max_length=(20))
    modelo = forms.CharField(max_length=(20))
    stock = forms.IntegerField()

class VendedoresForm(forms.Form):
    nombre = forms.CharField(max_length=(20))
    apellido = forms.CharField(max_length=(20))
    email = forms.EmailField()

class DistribuidoresForm(forms.Form):
    empresa = forms.CharField(max_length=(20))
    ingreso = forms.IntegerField()