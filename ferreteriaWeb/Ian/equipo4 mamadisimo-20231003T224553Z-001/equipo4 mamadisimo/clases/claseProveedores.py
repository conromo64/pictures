#Crea la clase del proveedor
class Proveedor (object):
    #Define las propiedades y variables de la clase
    def __init__(self,claveProveedor,nombre,razonSocial,rfc,direccion,telefono,tipo):
        self.claveProveedor = claveProveedor
        self.nombre = nombre
        self.razonSocial = razonSocial
        self.rfc = rfc
        self.direccion = direccion
        self.telefono = telefono
        self.tipo = tipo
    #Asignacion de los metodos de la clase
    def setClaveProveedor(self,claveProveedor):
        self.claveProveedor = claveProveedor     
    def setNombre (self,nombre):
        self.nombre = nombre     
    def setRazonSocial (self,razonSocial):
        self.razonSocial = razonSocial     
    def setRfc (self,rfc):
        self.rfc = rfc     
    def setDireccion (self,direccion):
        self.direccion = direccion
    def setTelefono (self,telefono):
        self.telefono = telefono
    def setTipo (self,tipo):
        self.tipo = tipo

    #Obtencion de las definiciones de las clases
    def getClaveProveedor (self):
        return self.claveProveedor      
    def getNombre (self):
        return self.nombre      
    def getRazonSocial (self):
        return self.razonSocial      
    def getRfc (self):
        return self.rfc      
    def getDireccion (self):
        return self.direccion
    def getTelefono (self):
        return self.telefono
    def getTipo (self):
        return self.tipo

#Da de alta proveedor
def altaProveedor(proveedores, proveedoresT):
    import clases.claseTipoProveedor

    #Pide los datos al usuario
    auxclaveProveedor = int(input("Dame la clave: "))
    auxNombre = input("Dame el nombre: ")
    auxrazonSocial = input("Ingresa la razon social: ")
    auxrfc = input("Ingresa el rfc: ")
    auxdireccion = input("Dame la direccion: ")
    auxtelefono = input("Dame el telefono: ")

    clases.claseTipoProveedor.imprimirTipoProveedores(proveedoresT)
    auxtipo=int(input("Dame la clave del tipo de proveedor: "))
    while(clases.claseTipoProveedor.buscarTipoProveedor(auxtipo, proveedoresT) == -1):
        print("La clave no existe")
        auxtipo=int(input("Dame la clave del tipo de proveedor: "))

    # Agregamos los datos de las auxiliares de cada campo a la lista 
    proveedores.append(Proveedor(auxclaveProveedor,auxNombre,auxrazonSocial,auxrfc,auxdireccion,auxtelefono,auxtipo))
    #Imprime la tabla y regresa la lista
    return proveedores

# Función para imprimir una tabla con los datos de los proveedors.
def imprimirProveedor(proveedores):
    print("\nTabla de proveedores\n")

    # Imprimir encabezados de la tabla.
    print("-" * 124)
    print("|{:<5}|{:<20}|{:<33}|{:<14}|{:<27}|{:<11}|{:<6}|".format(
        "Clave", "Nombre y ap.Paterno", "razon social", "RFC", "Direccion", "Telefono", "claveT"))
    print("-" * 124)

    # Imprimir los datos de cada proveedor en filas.
    for ind in range(len(proveedores)):
        print(f"|{proveedores[ind].getClaveProveedor():<5}|{proveedores[ind].getNombre():<20}|{proveedores[ind].getRazonSocial():<33}|{proveedores[ind].getRfc():<14}|{proveedores[ind].getDireccion():<27}|{proveedores[ind].getTelefono():<11}|{proveedores[ind].getTipo():<6}| ")
        print("-" * 124)

#Busca el proveedor
def buscarProveedor(auxIde,proveedor):
    #Busca a base de la posicion y la clave o numero de control el proveedor
    indice = -1
    for ind in range(0,len(proveedor),1):
        if(proveedor[ind].getClaveProveedor()==auxIde):
            indice = ind
    return indice

#Modifica un proveedor de la lista
def modificarProveedor(proveedor, proveedoresT):
    import clases.claseTipoProveedor
    #Imprime, ingresa e busca la clave para modificar en la lista
    imprimirProveedor(proveedor)
    ide = int(input("Dame el numero del proveedor a modificar: "))
    ind =buscarProveedor(ide,proveedor)
    if(ind!=-1):
        #Incerta cada uno de los datos que se les pide al usuario
        auxclaveProveedor = int(input("Dame la clave: "))
        auxNombre = input("Dame el nombre: ")
        auxrazonSocial = input("Ingresa la razon social: ")
        auxrfc = input("Ingresa el rfc: ")
        auxdireccion = input("Deme la direccion: ")
        auxtelefono = input("Deme el telefono: ")

        
        clases.claseTipoProveedor.imprimirTipoProveedores(proveedoresT)
        auxtipo=int(input("Dame la clave del tipo de proveedor: "))
        while(clases.claseTipoProveedor.buscarTipoProveedor(auxtipo, proveedoresT) == -1):
            print("La clave no existe")
            auxtipo=int(input("Dame la clave del tipo de proveedor: "))

        #Inserta las nuevas capturas
        proveedor[ind].setClaveProveedor(auxclaveProveedor)
        proveedor[ind].setNombre(auxNombre)
        proveedor[ind].setRazonSocial(auxrazonSocial)
        proveedor[ind].setRfc(auxrfc)
        proveedor[ind].setDireccion(auxdireccion)
        proveedor[ind].setTelefono(auxtelefono)
        proveedor[ind].setTipo(auxtipo)


    #si no lo encuentra muestra un mensaje
    else:
        print("El número de proveedor no existe")

    return proveedor

#Borra un proveedor de la lista
def borrarProveedor(proveedor):
   #Borra de la lista a base de la clave o numero de control
   imprimirProveedor(proveedor)
   auxNumControl = int(input("Dame el numero de control del proveedor que desea borrar : "))
   indice = buscarProveedor(auxNumControl,proveedor)
   if indice != -1:
       # Eliminar los datos del proveedor de la lista
       del proveedor[indice]
   else:
       print("Numero de control no exsixte")
   imprimirProveedor(proveedor)
   return proveedor