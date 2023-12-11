#importa las clases
from clases.claseArticulo import *
from clases.claseTipoArticulos import *
from clases.claseTipoUnidad import *
from clases.claseCliente import *
from clases.claseTipoCliente import *
from clases.claseProveedores import *
from clases.claseTipoProveedor import *

def creaJsonArticulo(listaArticulos):
    # Importa el módulo 'json' y modulo manipula archivo anterior
    import json
    import manipula.manipulaArchivo 
    #crea una lista 
    lista =[]
    #itera la lista 
    for articulo in listaArticulos:
        #Inicia una cadena jsonstr 
        jsonStr = '{ '
        jsonStr = jsonStr+'"ClaveArticulo"  :  '+str(articulo.getClaveArticulo())+', '
        jsonStr = jsonStr+'"Descripcion"  :  "'+str(articulo.getDescripcion())+'", '
        jsonStr = jsonStr+'"Costo"  :  '+str(articulo.getCosto())+', '
        jsonStr = jsonStr+'"PrecioMayoreo"  :  '+str(articulo.getPrecioMayoreo())+', '
        jsonStr = jsonStr+'"PrecioMenudeo"  :  '+str(articulo.getPrecioMenudeo())+', '
        jsonStr = jsonStr+'"ExistenciaAlmacen"  :  '+str(articulo.getExistenciaAlmacen())+', '
        jsonStr = jsonStr+'"ExistenciaPisoVenta"  :  '+str(articulo.getExistenciaPisoVenta())+', '
        jsonStr = jsonStr+'"CveTipoUnidad"  :  '+str(articulo.getClaveTipoUnidad())+','
        jsonStr = jsonStr+'"CveTipoProveedor"  :  '+str(articulo.getClaveProveedor())+', '
        jsonStr = jsonStr+'"CveTipoArticulo"  :  '+str(articulo.getClaveTipoArticulo())+' }'
        #Guarda los datos 
        lista.append(jsonStr)
    #esta ruta se tiene que cambiar dependiendo de el dispositivo 
    ruta = r"archivoTxt\articulos.txt"
    manipula.manipulaArchivo.creaArchivo(ruta,lista)

def leeJsonArticulos():
   # Importa modulo json y manipula archivo
    import json
    import manipula.manipulaArchivo 
    #Crea una ruta la cual se debe de cambiar para ejecutarlo
    ruta = r"archivoTxt\articulos.txt"
    # Lee las lineas de la ruta y despues las almacena     
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    #Crea una lista vacia con el nobre de datos 
    datos = []
    #Itera cada linea de la lista lineas
    for linea in lineas:
        # Cambia la cadena json en  un diccionario phyton 
        jsonDict = json.loads(linea)
        #Extra los valores
        auxClaveArticulo=jsonDict['ClaveArticulo']
        auxDescripcion=jsonDict['Descripcion']
        auxCosto=jsonDict['Costo']
        auxPrecioMayoreo=jsonDict['PrecioMayoreo']
        auxPrecioMenudeo=jsonDict['PrecioMenudeo']
        auxExiatenciaAlmacen=jsonDict['ExistenciaAlmacen']
        auxExistenciaPisoVenta=jsonDict['ExistenciaPisoVenta']
        auxCveTipoUnidad=jsonDict['CveTipoUnidad']
        auxCveTipoProveedor=jsonDict['CveTipoProveedor']
        auxCveTipoArticulo=jsonDict['CveTipoArticulo']
        #Guarda los datos en la lista "datos"
        datos.append(articulo(auxClaveArticulo,auxDescripcion,auxCosto,auxPrecioMayoreo, auxPrecioMenudeo, auxExiatenciaAlmacen, auxExistenciaPisoVenta, auxCveTipoUnidad, auxCveTipoProveedor, auxCveTipoArticulo))

    return datos


def creaJsonTipoArticulo(listaArticulosT):
    import manipula.manipulaArchivo 
    lista = []
    for articuloT in listaArticulosT:
        jsonStr = '{ '
        jsonStr = jsonStr + '"CveTipoArticulo" : ' + str(articuloT.getCveTipoArticulo()) + ', '
        jsonStr = jsonStr + '"DescripcionTipoArticulo" : "' + str(articuloT.getDescripcion()) + '" }' 
        lista.append(jsonStr)
    # Esta ruta se tiene que cambiar dependiendo del dispositivo 
    ruta = r"archivoTxt\TipoArticulos.txt"
    manipula.manipulaArchivo.creaArchivo(ruta, lista)


def leeJsonTipoArticulo():
    import json
    import manipula.manipulaArchivo 
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoArticulos.txt"
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    datos = []
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxCveTipoArticulo=jsonDict['CveTipoArticulo']
        auxDescripcion=jsonDict['DescripcionTipoArticulo']
        datos.append(TipoArticulo(auxCveTipoArticulo, auxDescripcion))
    return datos


def creaJsonTipoUnidad(listaUnidades):
    import manipula.manipulaArchivo 
    lista = []
    for unidades in listaUnidades:
        jsonStr = '{ '
        jsonStr = jsonStr + '"CveTipoUnidad" : ' + str(unidades.getCveTipoUnidad()) + ', '
        jsonStr = jsonStr + '"DescripcionUnidad" : "' + str(unidades.getDescripcionUnidad()) + '" }'
        lista.append(jsonStr)
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoUnidades.txt"
    manipula.manipulaArchivo.creaArchivo(ruta,lista)
    
def leeJsonTipoUnidad():
    import json
    import manipula.manipulaArchivo 
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoUnidades.txt"
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    datos = []
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxCveTipoUnidad=jsonDict['CveTipoUnidad']
        auxDescripcionUnidad=jsonDict['DescripcionUnidad']
        datos.append(TipoUnidad(auxCveTipoUnidad, auxDescripcionUnidad))
    return datos


def creaJsonCliente(listaclientes):
    import json
    import manipula.manipulaArchivo 
    lista = []
    for cliente in listaclientes:
        jsonStr = '{ '
        jsonStr = jsonStr + '"numControl" : ' + str(cliente.getNumControl()) + ', '
        jsonStr = jsonStr + '"nombre" : "' + str(cliente.getNombre()) + '", '
        jsonStr = jsonStr + '"apPaterno" : "' + str(cliente.getApMaterno()) + '", ' 
        jsonStr = jsonStr + '"apMaterno" : "' + str(cliente.getApMaterno()) + '", ' 
        jsonStr = jsonStr + '"tipo" : ' + str(cliente.getTipo()) + ' }'
        lista.append(jsonStr)
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\clientes.txt"
    manipula.manipulaArchivo.creaArchivo(ruta,lista)
    
def leeJsonClientes():
    import json
    import manipula.manipulaArchivo 
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\clientes.txt"
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    datos = []
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxNumControl=jsonDict['numControl']
        auxNombre=jsonDict['nombre']
        auxApPaterno=jsonDict['apPaterno']
        auxApMaterno=jsonDict['apMaterno']
        auxTipo=jsonDict['tipo']
        datos.append(cliente(auxNumControl, auxNombre, auxApPaterno, auxApMaterno, auxTipo))
    return datos


def creaJsonTipoClientes(listaClientes):
    import manipula.manipulaArchivo 
    lista = []
    for clientes in listaClientes:
        jsonStr = '{ '
        jsonStr = jsonStr + '"CveTipoCliente" : ' + str(clientes.getCveTipoCliente()) + ', '
        jsonStr = jsonStr + '"DescripcionTipoCliente" : "' + str(clientes.getDescripcion()) + '" }'
        lista.append(jsonStr)
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoCliente.txt"
    manipula.manipulaArchivo.creaArchivo(ruta,lista)

def leeJsonTipoClientes():
    import json
    import manipula.manipulaArchivo 
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoCliente.txt"
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    datos = []
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxCveTipoCliente=jsonDict['CveTipoCliente']
        auxDescripcion=jsonDict['DescripcionTipoCliente']
        datos.append(TipoCliente(auxCveTipoCliente, auxDescripcion))
    return datos


def creaJsonProveedor(listaProveedor):
    import json
    import manipula.manipulaArchivo 
    lista =[]
    for proveedor in listaProveedor:
        jsonStr = '{ '
        jsonStr = jsonStr+'"ClaveProveedor"  :  '+str(proveedor.getClaveProveedor())+', '
        jsonStr = jsonStr+'"Nombre"  :  "'+str(proveedor.getNombre())+'", '
        jsonStr = jsonStr+'"RazonSocial"  :  "'+str(proveedor.getRazonSocial())+'", '
        jsonStr = jsonStr+'"RFC"  :  "'+str(proveedor.getRfc())+'", '
        jsonStr = jsonStr+'"Direccion"  :  "'+str(proveedor.getDireccion())+'", '
        jsonStr = jsonStr+'"Telefono"  :  '+str(proveedor.getTelefono())+', '
        jsonStr = jsonStr+'"Tipo"  :  '+str(proveedor.getTipo())+' }'
        lista.append(jsonStr)
    ruta = r"archivoTxt\proveedor.txt"
    #esta ruta se tiene que cambiar dependienod el dispositivo 
    manipula.manipulaArchivo.creaArchivo(ruta,lista)

def leeJsonProveedor():
    import json
    import manipula.manipulaArchivo 
    ruta = r"archivoTxt\proveedor.txt"
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    datos = []
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxclaveProveedor=jsonDict['ClaveProveedor']
        auxNombre=jsonDict['Nombre']
        auxrazonSocial=jsonDict['RazonSocial']
        auxrfc=jsonDict['RFC']
        auxdireccion=jsonDict['Direccion']
        auxtelefono=jsonDict['Telefono']
        auxtipo=jsonDict['Tipo']
        datos.append(Proveedor(auxclaveProveedor,auxNombre,auxrazonSocial,auxrfc, auxdireccion, auxtelefono, auxtipo))


    return datos


def creaJsonTipoProveedor(listaProveedores):
    import manipula.manipulaArchivo 
    lista = []
    for proveedores in listaProveedores:
        jsonStr = '{ '
        jsonStr = jsonStr + '"CveTipoProveedor" : ' + str(proveedores.getCveTipoProveedor()) + ', '
        jsonStr = jsonStr + '"DescripcionTipoProveedor" : "' + str(proveedores.getDescripcion()) + '" }'
        lista.append(jsonStr)
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoProveedores.txt"
    manipula.manipulaArchivo.creaArchivo(ruta,lista)

def leeJsonTipoProveedor():
    import json
    import manipula.manipulaArchivo 
    #esta ruta se tiene que cambiar dependiendo el dispositivo 
    ruta=r"archivoTxt\TipoProveedores.txt"
    lineas = manipula.manipulaArchivo.leerArchivo(ruta)
    datos = []
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxCveTipoProveedor=jsonDict['CveTipoProveedor']
        auxDescripcion=jsonDict['DescripcionTipoProveedor']
        datos.append(TipoProveedor(auxCveTipoProveedor, auxDescripcion))
    return datos