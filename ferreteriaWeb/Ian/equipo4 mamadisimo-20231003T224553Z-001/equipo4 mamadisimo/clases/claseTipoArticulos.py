# Crea una clase con el nombre de "TipoArticulo"
class TipoArticulo(object):
   # Definimos propiedades y valores
    def __init__(self, cveTipoArticulo, descripcion):
        self.cveTipoArticulo =cveTipoArticulo
        self.descripcion = descripcion
        
    # Asignacion de los metodos de la clase
    def setCveTipoArticulo(self, cveTipoArticulo):
        self.cveTipoArticulo = cveTipoArticulo

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    # Obtencion de las definiciones de las clases
    def getCveTipoArticulo(self):
        return self.cveTipoArticulo

    def getDescripcion(self):
        return self.descripcion

def get_dato(mensaje):
    while True:
        try:
            dato = int(input(mensaje))
            break  # Salir del bucle si la entrada es un número válido
        except ValueError:
            print("Dato invalido. Por favor, ingresa un número.")
        # Aquí continúa el código después de haber obtenido un número válido.
    return dato

# Da de alta proveedor
def altaTipoArticulos(articulosT):
    # Pide los datos
    menCveTipoArticulo = "Dame tu clave del tipo de articulo: "
    auxCveTipoArticulo = 0
    auxCveTipoArticulo = get_dato(menCveTipoArticulo) 
    auxDescripcion = input("Dame la descripcion: ")

    #Agregamos los datos a la lista
    articulosT.append(TipoArticulo(auxCveTipoArticulo, auxDescripcion))

    return articulosT

def imprimirTipoArticulos(articulosT):
# Imprimir encabezados de la tabla.
    print("\nTabla tipo articulos \n")
    print("-" * 24)
    print("|{:<6} | {:<12} |".format(
        "Clave", "Descripcion"))
    print("-" * 24)
    
    # Imprimir los datos de cada cliente en filas.
    for ind in range(0, len(articulosT), 1):
        print(f"|{articulosT[ind].getCveTipoArticulo():<6} | {articulosT[ind].getDescripcion():<12} |")
        print("-" * 24)
    return articulosT

def buscarTipoArticulo(auxIde, articulosT):
    indice = -1
    for ind in range(0, len(articulosT), 1):
        if (articulosT[ind].getCveTipoArticulo() == auxIde):
            indice = ind
    return indice

def modificarTipoArticulo(articulosT):
    imprimirTipoArticulos(articulosT)
    print("")
    #Busca a base de la posicion y la clave o numero de el tipo de el tipo articulo
    ide = int(input("Dame la clave del tipo de articulo a modificar : "))
    ind = buscarTipoArticulo(ide, articulosT)

    if (ind != -1):
        auxCveTipoArticulo = int(input("Dame la clave del articulo " + str(articulosT[ind].getCveTipoArticulo()) + "<- "))
        auxDescripcion = input("Dame la descripcion del articulo " + str(articulosT[ind].getDescripcion()) + "<- ")


        articulosT[ind].setCveTipoArticulo(auxCveTipoArticulo)
        articulosT[ind].setDescripcion(auxDescripcion)


    else:
        print("la clave del tipo de Articulo no existe")

    return articulosT

def borrarTipoArticulo(articulosT):
    imprimirTipoArticulos(articulosT)
    print("")
    #Busca el tipo articulos
    auxCveTipoArticulo = int(input("Dame la clave del tipo de articulo que desea borrar: "))
    indice = buscarTipoArticulo(auxCveTipoArticulo, articulosT)
    #Borra articulo
    if indice != -1:
        del articulosT[indice]
    #No se encontro la clave
    else:
        print("la clave del tipo de articulo no existe")
    return articulosT
