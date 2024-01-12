from django import forms

class BebidasFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    marca = forms.CharField(max_length=60)
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()

class ComidasFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    marca = forms.CharField(max_length=60)
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()

class AccesoriosFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()