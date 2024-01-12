from django.urls import path
from AppCoder.views import *


urlpatterns = [

    path('', inicio, name="Inicio"),
    path('bebidasSinAlcohol/', formu_bebidasSinAlcohol, name="Bebidas Sin Alcohol"),
    path('bebidasConAlcohol/', formu_bebidasConAlcohol, name="Bebidas Con Alcohol"),
    path('accesorios/', formu_accesorios, name="Accesorios"),
    path('comidas/', formu_comidas, name="Comidas"),
    path('buscarBebidas/', busquedaBebidas, name="Buscar Bebidas"),
    path("resultados/", resultados, name="Resultados Busqueda"),

]