from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *


# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def bebidasConAlcohol(request):
    
    return render(request, "AppCoder/bebidasConAlcohol.html")

def bebidasSinAlcohol(request):

    return render(request, "AppCoder/bebidasSinAlcohol.html")

def comidas(request):

    return render(request, "AppCoder/comidas.html")

def accesorios(request):

    return render(request, "AppCoder/accesorios.html")

def formu_bebidasConAlcohol(request):

    if request.method == "POST":

        formulario1 = BebidasFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            producto = BebidasConAlcohol(nombre=info["nombre"],
                             marca=info["marca"],
                             cantidad=info["cantidad"],
                             precio=info["precio"]       
                             )
            producto.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = BebidasFormulario()

    return render(request, "AppCoder/bebidasConAlcohol.html", {"form1":formulario1})

def formu_bebidasSinAlcohol(request):

    if request.method == "POST":

        formulario2 = BebidasFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            producto = BebidasSinAlcohol(nombre=info["nombre"],
                             marca=info["marca"],
                             cantidad=info["cantidad"],
                             precio=info["precio"]       
                             )
            producto.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario2 = BebidasFormulario()

    return render(request, "AppCoder/bebidasSinAlcohol.html", {"form2":formulario2})

def formu_comidas(request):

    if request.method == "POST":

        formulario3 = ComidasFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            producto = Comidas(nombre=info["nombre"],
                             marca=info["marca"],
                             cantidad=info["cantidad"],
                             precio=info["precio"]       
                             )
            producto.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario3 = ComidasFormulario()

    return render(request, "AppCoder/comidas.html", {"form3":formulario3})

def formu_accesorios(request):

    if request.method == "POST":

        formulario4 = AccesoriosFormulario(request.POST)

        if formulario4.is_valid():

            info = formulario4.cleaned_data

            producto = Accesorios(nombre=info["nombre"],
                             cantidad=info["cantidad"],
                             precio=info["precio"]       
                             )
            producto.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario4 = AccesoriosFormulario()

    return render(request, "AppCoder/accesorios.html", {"form4":formulario4})


def busquedaBebidas(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):
    
    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        productos = BebidasConAlcohol.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/inicio.html", {"productos":productos, "bebida":nombre})

    else:

        respuesta = "No enviaste datos."



    return HttpResponse(respuesta)