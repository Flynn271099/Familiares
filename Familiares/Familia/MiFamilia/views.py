from django.shortcuts import render
from MiFamilia.models import Familia

# Create your views here.

def familiares(request):

    papa = Familia(nombre = "Maximiliano Ariel", apellido = "Flynn", edad = 54, cumpleaños = "1968-02-26")
    mama = Familia(nombre = "María Evangelina", apellido = "Robles", edad = 44, cumpleaños = "1974-07-07")
    hermana = Familia(nombre = "María Agustina", apellido = "Flynn", edad = 24, cumpleaños = "1997-12-31")
    hermano = Familia(nombre = "Facundo", apellido = "Flynn", edad = 14, cumpleaños = "2008-02-01")
    hermanita = Familia(nombre = "Emma", apellido = "Flynn", edad = 10, cumpleaños = "2012-08-02")

    return render(request, "MiFamilia/index.html", {"familia":[papa, mama, hermana, hermano]})