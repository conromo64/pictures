# Define una clase llamada cliente, para que actue como plantilla para crear objetos
class cliente(object):
       # Define las propiedades y variables, para que las variables tangan sus propias copias con valores específicos para ese objeto.
    def __init__(self, numControl, nombre, apPaterno, apMaterno, tipo):
        self.numControl = numControl
        self.nombre = nombre
        self.apPaterno = apPaterno
        self.apMaterno = apMaterno
        self.tipo = tipo
   
    # Definimos los metodos de asignacion para las variables der la clase  para modificar los objetos 
    def setNumControl(self, numControl):
        self.numControl = numControl

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApPaterno(self, apPaterno):
        self.apPaterno = apPaterno

    def setApMaterno(self, apMaterno):
        self.apMaterno = apMaterno

    def setTipo(self, tipo):
        self.tipo = tipo
   
    # Metodo se encarga de actualizar los valores
    def getNumControl(self):
        return self.numControl

    def getNombre(self):
        return self.nombre

    def getApPaterno(self):
        return self.apPaterno

    def getApMaterno(self):
        return self.apMaterno

    def getTipo(self):
        return self.tipo

def get_datoI(mensaje):
    while True:
        try:
            dato = int(input(mensaje))
            break  # Salir del bucle si la entrada es un número válido
        except ValueError:
            print("Dato invalido. Por favor, ingresa un número.")
        # Aquí continúa el código después de haber obtenido un número válido.
    return dato

# Función para agregar un nuevo articulo a la lista 'articulos'.
def altaCliente(clientes, clientesT):
    import clases.claseTipoCliente
     
    menNumControl = "Dame el numero de control: "
    auxNumControl = 0
    auxNumControl = get_datoI(menNumControl)

    auxNombre = input("Dame el nombre : ")
    auxApPaterno = input("Ingresa el apellido Paterno: ")
    auxApMaterno = input("Ingresa el apellido Materno: ")

    clases.claseTipoCliente.imprimirTipoClientes(clientesT)
    
    menTipo = "Dame el numero de control del tipo del cliente: "
    auxTipo = 0
    auxTipo = get_datoI(menTipo)
    while(clases.claseTipoCliente.buscarTipoClientes(auxTipo, clientesT) == -1):
        print("el numero de control no existe")
        auxTipo = get_datoI(menTipo)

    clientes.append(cliente(auxNumControl, auxNombre, auxApPaterno, auxApMaterno, auxTipo))

    return clientes

# Función para imprimir una tabla con los datos de los clientes.
def imprimirTabla(clientes):
    print("\nTabla cliente\n")
    # Imprimir encabezados de la tabla.
    print("-" * 84)
    print("|{:<17} | {:<20} | {:<12} | {:<12} | {:<8} |".format(
        "Num. Control", "Nombre", "Ap. Paterno", "Ap. Materno", "claveT"))
    print("-" * 84)
    
    # Imprimir los datos de cada cliente en filas.
    for ind in range(0, len(clientes), 1):
        print(f"|{clientes[ind].getNumControl():<17} | {clientes[ind].getNombre():<20} | {clientes[ind].getApPaterno():<12} | {clientes[ind].getApMaterno():<12} | {clientes[ind].getTipo():<8} | ")
        print("-" * 84,"\n")

#Iera sobre los indices de la lista "clientes", para despues comprobar si el numero de control coincide con el en la posicion, en caso de no encontralo indice sera -1
def buscarCliente(auxIde, clientes):
    indice = -1
    for ind in range(0, len(clientes), 1):
        if (clientes[ind].getNumControl() == auxIde):
            indice = ind
    return indice

# Pide el numero de control de el cliente aplicando el codigo de bucaArticulos para despues actulizar los valores de la lista si no se encuentre saltara un mensajes de que no se a encontrado
def modificarCliente(clientes, clientesT):
    import clases.claseTipoCliente
    imprimirTabla(clientes)
         
    menNumControl = "Dame el numero de control del cliente a modificar: "
    auxNumControl = 0
    ide = get_datoI(menNumControl)
    ind = buscarCliente(ide, clientes)

    if (ind != -1):
             
        menNumControl = "Dame el numero de control " + str(clientes[ind].getNumControl()) + "<- "
        auxNumControl = 0
        auxNumControl = get_datoI(menNumControl)

        auxNombre = input("Dame el nombre " + str(clientes[ind].getNombre()) + "<- ")
        auxApPaterno = input("Ingresa el apellido Paterno " + str(clientes[ind].getApPaterno()) + "<- ")
        auxApMaterno = input("Ingresa el apellido Materno " + str(clientes[ind].getApMaterno()) + "<- ")

        clases.claseTipoCliente.imprimirTipoClientes(clientesT)
        menTipo = "Ingresa el tipo " + str(clientes[ind].getTipo()) + "<- "
        auxTipo = 0
        auxTipo = get_datoI(menTipo)
        while(clases.claseTipoCliente.buscarTipoClientes(auxTipo, clientesT) == -1):
            print("el numero de control no existe")
            menTipo = "Ingresa el tipo " + str(clientes[ind].getTipo()) + "<- "
            auxTipo = 0
            auxTipo = get_datoI(menTipo)

        clientes[ind].setNumControl(auxNumControl)
        clientes[ind].setNombre(auxNombre)
        clientes[ind].setApPaterno(auxApPaterno)
        clientes[ind].setApMaterno(auxApMaterno)
        clientes[ind].setTipo(auxTipo)

    else:
        print("El número de control no existe")

    return clientes

# Pide el numero de control de el cliente para bucarlo y proceder a eliminarlo, si no ess econtrado saltara un mensaje que no fue encontrado
def borrarCliente(clientes):

    imprimirTabla(clientes)
     
    menNumControl = "Dame el numero el numero de control del cliente que desea borrar: "
    auxNumControl = 0
    auxNumControl = get_datoI(menNumControl)

    indice = buscarCliente(auxNumControl, clientes)

    if indice != -1:
        del clientes[indice]
    else:
        print("Numero de control no existe")
    return clientes