#Crea la clase tipo unidad
class TipoUnidad(object):
    #Define las propiedades y variables de la clase
    def __init__(self, cveTipoUnidad, descripcionUnidad, ):
        self.cveTipoUnidad = cveTipoUnidad
        self.descripcionUnidad = descripcionUnidad
        
    #Asignacion de los metodos de la clase
    def setCveTipoUnidad(self, cveTipoUnidad):
        self.cveTipoUnidad = cveTipoUnidad

    def setDescripcion(self, descripcionUnidad):
        self.descripcionUnidad = descripcionUnidad
    
    #Obtencion de las definiciones de las clases
    def getCveTipoUnidad(self):
        return self.cveTipoUnidad

    def getDescripcionUnidad(self):
        return self.descripcionUnidad


#Da de alta unidad
def altaTipoUnidad(unidades):
    #Pide los datos al usuario
    auxCveTipoUnidad = int(input("Dame tu clave del tipo de unidad: "))
    auxDescripcionUnidad = input("Dame la descripcion de la unidad: ")
    #Guarda los datos en la lista
    unidades.append(TipoUnidad(auxCveTipoUnidad, auxDescripcionUnidad))

    return unidades

def imprimirTipounidades(unidades):
# Imprimir encabezados de la tabla.
    print("\nTabla tipo unidades \n")
    print("-" * 24)
    print("|{:<6} | {:<12} |".format(
        "clave", "Descripcion"))
    print("-" * 24)
    
    # Imprimir los datos de cada cliente en filas.
    for ind in range(0, len(unidades), 1):
        print(f"|{unidades[ind].getCveTipoUnidad():<6} | {unidades[ind].getDescripcionUnidad():<12} |")
        print("-" * 24)

#Busca el unidad
def buscarTipoUnidad(auxIde, unidades):
    indice = -1
    #Busca a base de la posicion y la clave o numero de control el unidad
    for ind in range(0, len(unidades), 1):
        if (unidades[ind].getCveTipoUnidad() == auxIde):
            indice = ind
    return indice

#Modifica un unidad de la lista
def modificarTipoUnidad(unidades):
    imprimirTipounidades(unidades)
    print("")
    #Imprime, ingresa e busca la clave para modificar en la lista
    ide = int(input("Dame el numero de la clave de la unidad "))
    ind = buscarTipoUnidad(ide, unidades)
    
    #Incerta cada uno de los datos que se les pide al usuario
    if (ind != -1):
        auxCveTipoUnidad = int(input("Dame la clave de la unidad " + str(unidades[ind].getCveTipoUnidad()) + "<- "))
        
        auxDescripcionUnidad = input("Dame la descripcion de la unidad " + str(unidades[ind].getDescripcionUnidad()) + "<- ")

        #Inserta las nuevas capturas
        unidades[ind].setCveTipoUnidad(auxCveTipoUnidad)
        unidades[ind].setDescripcion(auxDescripcionUnidad)

    #No se encontro la clave
    else:
        print("la clave del tipo de unidad no existe")

    print(auxCveTipoUnidad)
    return unidades

#Borra un unidad de la lista
def borrarTipounidades(unidades):
    imprimirTipounidades(unidades)
    print("")
   #Borra de la lista a base de la clave o numero de control
    auxCveTipoUnidad = int(input("Dame la clave del tipo de unidad que desea borrar: "))
    indice = buscarTipoUnidad(auxCveTipoUnidad, unidades)
    # Eliminar los datos del unidad de la lista
    if indice != -1:
        del unidades[indice]
    else:
        print("la clave del tipo de unidad no existe")
    return unidades
