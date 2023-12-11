from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido



def saludo2(request):
    p1=Persona("Martin","Contreras")
    hoy = datetime.datetime.now()
    plantilla=open('/Users/martincontrerasromo/misdocumentos/ferreteria/ferreteriaWeb/ferreteriaWeb/templates/hola.html')
    plt=Template(plantilla.read())
    plantilla.close()
    ctx=Context({"persona":p1,"ahora":hoy})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def saludo3(request):
    p1=Persona("Martin","Contreras")
    hoy = datetime.datetime.now()
    lista_temas=["plantillas","modelos","formularios","vistas","despliegue"]
    plantilla=open('/Users/martincontrerasromo/misdocumentos/ferreteria/ferreteriaWeb/ferreteriaWeb/templates/hola.html')
    plt=Template(plantilla.read())
    plantilla.close()
    ctx=Context({"persona":p1, "ahora":hoy,"temas":lista_temas })
    documento=plt.render(ctx)
    return HttpResponse(documento)



def saludo(request):
    documento="""<html>
        <body>
            <h1>
               hola mundo 
            </h1>
        </body>
    </html>"""
    return HttpResponse(documento)

def despedida(request):
  return HttpResponse("adios mundo")

def fecha(request):
    hoy = datetime.datetime.now()
    documento="""<html>
        <body>
            <h1>
                la fecha y hora es: %s
            </h1>
        </body>
    </html>""" % hoy
    return HttpResponse(documento)


def edad(request,actual,anio):
    diferencia=anio-2019
    futuro=actual+diferencia
    hoy = datetime.datetime.now()
    documento="""<html>
        <body>
            <h1>
                En el año %s tendras %s años
            </h1>
        </body>
    </html>""" % (anio,futuro)
    return HttpResponse(documento)