#Creamos una clase con el nombre de "Tipo Cliente"
class TipoCliente(object):
    #Definimos propiedades y valores
    def __init__(self, cveTipoCliente, descripcion):
        self.cveTipoCliente =cveTipoCliente
        self.descripcion = descripcion  
   
    # Asignacion de los metodos de la clase
    def setCveTipoCliente(self, cveTipoCliente):
        self.cveTipoCliente = cveTipoCliente

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    # Obtencion de las definiciones de las clases
    def getCveTipoCliente(self):
        return self.cveTipoCliente

    def getDescripcion(self):
        return self.descripcion


#Alta del tipo cliente
def altaTipoCliente(clientesT):
    #Pide los datos
    auxCveTipoCliente = int(input("Dame la clave del tipo de cliente: "))
    auxDescripcion = input("Dame la descripcion: ")

    #Guarda los datos
    clientesT.append(TipoCliente(auxCveTipoCliente, auxDescripcion))

    return clientesT

def imprimirTipoClientes(clientesT):
    print("\nTabla de tippo clientes\n")
# Imprimir encabezados de la tabla.
    print("-" * 24)
    print("|{:<6} | {:<12} |".format(
        "Clave", "Descripcion"))
    print("-" * 24)
    
    # Imprimir los datos de cada cliente en filas.
    for ind in range(0, len(clientesT), 1):
        print(f"|{clientesT[ind].getCveTipoCliente():<6} | {clientesT[ind].getDescripcion():<12} |")
        print("-" * 24)
    return clientesT

def buscarTipoClientes(auxIde, clientesT):
    indice = -1
    #Busca usando el metodo iteracion 
    for ind in range(0, len(clientesT), 1):
        if (clientesT[ind].getCveTipoCliente() == auxIde):
            indice = ind
    return indice

def modificarTipoClientes(clientesT):
    imprimirTipoClientes(clientesT)

    ide = int(input("Dame la clave del tipo de cliente a modificar: "))
    ind = buscarTipoClientes(ide, clientesT)
    #modica los datos
    if (ind != -1):
        auxCveTipoCliente= int(input("Dame la clave del tipo de cliente " + str(clientesT[ind].getCveTipoCliente()) + "<- "))
        auxDescripcion = input("Dame la descripcion del tipo de cliente " + str(clientesT[ind].getDescripcion()) + "<- ")


        clientesT[ind].setCveTipoCliente(auxCveTipoCliente)
        clientesT[ind].setDescripcion(auxDescripcion)

    #No encontro la clave
    else:
        print("la clave del tipo de cliente no existe")

    return clientesT

def borrarTipoClientes(clientesT):
    imprimirTipoClientes(clientesT)
    print("")
    #Busca cel cliente para borrarlo
    auxCveTipoCliente = int(input("Dame la clave del tipo de cliente que desea borrar: "))
    indice = buscarTipoClientes(auxCveTipoCliente, clientesT)
    
    if indice != -1:
        del clientesT[indice]
    else:
        print("la clave del tipo de cliente no existe")
    return clientesT
