from django import forms

class CajaForm(forms.Form):
    entrada = forms.IntegerField()
    salida = forms.IntegerField()
    motivo = forms.CharField(max_length=214)

class DistribuidoresForm(forms.Form):
    empresa = forms.CharField(max_length=200)