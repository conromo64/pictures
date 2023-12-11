#creamos una clase con el nombre de "tipo provedor"
class TipoProveedor(object):
    #Define las propiedades y variables de la clase
    def __init__(self, cveTipoProveedor, descripcion):
        self.cveTipoProveedor =cveTipoProveedor
        self.descripcion = descripcion
        
    #Asignacion de los metodos de la clase
    def setCveTipoProveedor(self, cveTipoProveedor):
        self.cveTipoProveedor = cveTipoProveedor

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    #Obtencion de las definiciones de las clases
    def getCveTipoProveedor(self):
        return self.cveTipoProveedor

    def getDescripcion(self):
        return self.descripcion


#Da de alta proveedor
def altaTipoProveedor(proveedoresT):
    #Pide los datos
    auxCveTipoProveedor = int(input("Dame la clave del tipo de proveedor: "))
    auxDescripcion = input("Dame la descripcion: ")

    #Guarda los datos en la lista
    proveedoresT.append(TipoProveedor(auxCveTipoProveedor, auxDescripcion))

    return proveedoresT

def imprimirTipoProveedores(proveedoresT):
# Imprimir encabezados de la tabla.
    print("\nTabla tipo proveedores \n")
    print("-" * 24)
    print("|{:<6} | {:<12} |".format(
        "Clave", "Descripcion"))
    print("-" * 24)
    
    # Imprimir los datos de cada cliente en filas.
    for ind in range(0, len(proveedoresT), 1):
        print(f"|{proveedoresT[ind].getCveTipoProveedor():<6} | {proveedoresT[ind].getDescripcion():<12} |")
        print("-" * 24)

def buscarTipoProveedor(auxIde, proveedoresT):
    indice = -1
    #Busca a base de la posicion y la clave o numero de control el proveedor
    for ind in range(0, len(proveedoresT), 1):
        if (proveedoresT[ind].getCveTipoProveedor() == auxIde):
            indice = ind
    return indice

#Modifica un proveedor de la lista
def modificarTipoProveedor(proveedoresT):
    imprimirTipoProveedores(proveedoresT)
    print("")
    #Imprime, ingresa e busca la clave para modificar en la lista
    ide = int(input("Dame la clave del tipo de proveedor a modificar: "))
    ind = buscarTipoProveedor(ide, proveedoresT)

    if (ind != -1):
        auxCveTipoProveedor = int(input("Dame la clave del proveedor " + str(proveedoresT[ind].getCveTipoProveedor()) + "<- "))
        auxDescripcion = input("Dame la descripcion del proveedor " + str(proveedoresT[ind].getDescripcion()) + "<- ")

        #Inserta las nuevas capturas
        proveedoresT[ind].setCveTipoProveedor(auxCveTipoProveedor)
        proveedoresT[ind].setDescripcion(auxDescripcion)

    #No se encontro la clave
    else:
        print("La clave del tipo de proveedor no existe")

    return proveedoresT

#Borra un proveedor de la lista
def borrarTipoProveedores(proveedoresT):
    imprimirTipoProveedores(proveedoresT)
    print("")
   #Borra de la lista a base de la clave o numero de control
    auxCveTipoProveedor = int(input("Dame la clave del tipo de proveedor que desea borrar: "))
    indice = buscarTipoProveedor(auxCveTipoProveedor, proveedoresT)
    # Eliminar los datos del proveedor de la lista
    if indice != -1:
        del proveedoresT[indice]
    else:
        print("La clave del tipo de proveedor no existe")
    return proveedoresT
