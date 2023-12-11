from django.http import HttpResponse
import requests
import datetime
import json
from django.template import Template, Context
pagina = 0

def menu(request):
    plantilla=open('/Users/martincontrerasromo/misdocumentos/ferreteria/ferreteriaWeb/ferreteriaWeb/templates/menu.html')
    plt=Template(plantilla.read())
    plantilla.close()
    ctx=Context({})
    documento=plt.render(ctx)
    return HttpResponse(documento)



'''def articulos(request):        
    #pagina = 1  # Puedes ajustar la página según tus necesidades
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=d78cfb8acb70922ed2c45fc903e9bcea&language=es-MX'
    peliculas = requests.get(url)
    print("----------------------------------------------------------")
    # Verifica si la solicitud fue exitosa (código de estado 200)
    if peliculas.status_code == 200:
        for pelicula in peliculas:
            jsonDict = json.loads(pelicula)
            aux_page = jsonDict['page']
            aux_results = jsonDict['results']
            print(aux_page)
            print(aux_results)
        plantilla=open('/Users/martincontrerasromo/misdocumentos/ferreteria/ferreteriaWeb/ferreteriaWeb/templates/articulo.html')
        plt=Template(plantilla.read())
        plantilla.close()
        ctx=Context({"peliculas":peliculas})
        documento=plt.render(ctx)
        return HttpResponse(documento)
    else:
        print(f'Error en la solicitud. Código de estado: {peliculas.status_code}')
'''

##########################

def peliculas(request):
    try:
        global pagina 
        pagina = pagina+1  # Puedes ajustar esto según tus necesidades
        api_key = 'd78cfb8acb70922ed2c45fc903e9bcea'
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=es-MX&page={pagina}'
        # Realizar la llamada a la API
        respuesta = requests.get(url)
        resultados = respuesta.json()
        #print(resultados)
        peliculas = resultados['results']
        print(peliculas)
        plantilla=open('/Users/martincontrerasromo/misdocumentos/ferreteria/ferreteriaWeb/ferreteriaWeb/templates/articulo.html')
        plt=Template(plantilla.read())
        plantilla.close()
        ctx=Context({"peliculas":peliculas})
        documento=plt.render(ctx)
        return HttpResponse(documento)
    except Exception as e:
        # Manejar errores según tus necesidades
        print('Error en la solicitud. Código de estado: {peliculas.status_code}')
   

def peliculas_ant(request):
    try:
        global pagina 
        if (pagina>1):
            pagina = pagina-1  # Puedes ajustar esto según tus necesidades
        api_key = 'd78cfb8acb70922ed2c45fc903e9bcea'
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=es-MX&page={pagina}'
        # Realizar la llamada a la API
        respuesta = requests.get(url)
        resultados = respuesta.json()
        #print(resultados)
        peliculas = resultados['results']
        print(peliculas)
        plantilla=open('/Users/martincontrerasromo/misdocumentos/ferreteria/ferreteriaWeb/ferreteriaWeb/templates/articulo.html')
        plt=Template(plantilla.read())
        plantilla.close()
        ctx=Context({"peliculas":peliculas})
        documento=plt.render(ctx)
        return HttpResponse(documento)
    except Exception as e:
        # Manejar errores según tus necesidades
        print('Error en la solicitud. Código de estado: {peliculas.status_code}')
