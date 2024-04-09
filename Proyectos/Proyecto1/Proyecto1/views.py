from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola mundo")

def hoy(request):
    fecha = datetime.now()
    return HttpResponse(f"El dia de hoy es:{fecha}")

def name(request, nombre):
    return HttpResponse(f"Tu nombre es:{nombre}")

def prueba(request):
    nombre = "jara"

    pais = "argentina"

    listaedades = [20,22,21,23,24,25]

    diccionario = {"name":nombre, "country":pais, "ages":listaedades}

    miHtml = open("C:/Users/Valen/Desktop/Proyectos/Proyecto1/Proyecto1/plantillas/plantilla1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    plantilla = loader.get_template("plantilla1.html")

    documento = plantilla.render(diccionario)

    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
