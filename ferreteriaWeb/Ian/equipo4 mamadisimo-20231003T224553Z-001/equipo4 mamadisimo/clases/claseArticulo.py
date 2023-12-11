# Define una clase llamada articulo, para que actue como plantilla para crear objetos
class articulo (object):
    # Define las propiedades y variables, para que las variables tangan sus propias copias con valores específicos para ese objeto.
    def __init__(self, claveArticulo, descripcion, costo, precioMayoreo, precioMenudeo, existenciaAlmacen, existenciaPisoVenta, cveTipoUnidad, cveProveedor, cveTipoArticulo) :
        self.claveArticulo = claveArticulo
        self.descripcion = descripcion
        self.costo = costo
        self.precioMayoreo = precioMayoreo
        self.precioMenudeo = precioMenudeo
        self.existenciaAlmacen = existenciaAlmacen
        self.existenciaPisoVenta = existenciaPisoVenta
        self.cveTipoUnidad = cveTipoUnidad
        self.cveProveedor = cveProveedor
        self.cveTipoArticulo = cveTipoArticulo

    # Definimos los metodos de asignacion para las Variables de la clase  para modificar los objetos 
    def setClaveArticulo(self, claveArticulo):
        self.claveArticulo = claveArticulo

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
        
    def setCosto(self, costo):
        self.costo = costo

    def setPrecioMayoreo(self, precioMayoreo):
        self.precioMayoreo = precioMayoreo

    def setPrecioMenudeo(self, precioMenudeo):
        self.precioMenudeo = precioMenudeo

    def setExistenciaAlmacen(self, existenciaAlmacen):
        self.existenciaAlmacen = existenciaAlmacen

    def setExistenciaPisoVenta(self, existenciaPisoVenta):
        self.existenciaPisoVenta = existenciaPisoVenta

    def setCveTipoUnidad(self, cveTipoUnidad):
        self.cveTipoUnidad = cveTipoUnidad

    def setCveProveedor(self, cveProveedor):
        self.cveProveedor = cveProveedor

    def setCveTipoArticulo(self, cveTipoUnidad):
        self.cveTipoUnidad = cveTipoUnidad

    # Metodo se encarga de actualizar los valores
    def getClaveArticulo(self):
        return self.claveArticulo

    def getDescripcion(self):
        return self.descripcion

    def getCosto(self):
        return self.costo

    def getPrecioMayoreo(self):
        return self.precioMayoreo

    def getPrecioMenudeo(self):
        return self.precioMenudeo

    def getExistenciaAlmacen(self):
        return self.existenciaAlmacen

    def getExistenciaPisoVenta(self):
        return self.existenciaPisoVenta

    def getClaveTipoUnidad(self):
        return self.cveTipoUnidad

    def getClaveProveedor(self):
        return self.cveProveedor

    def getClaveTipoArticulo(self):
        return self.cveTipoArticulo

def get_datoI(mensaje):
    while True:
        try:
            dato = int(input(mensaje))
            break  # Salir del bucle si la entrada es un número válido
        except ValueError:
            print("Dato invalido. Por favor, ingresa un número.")
        # Aquí continúa el código después de haber obtenido un número válido.
    return dato

def get_datoF(mensaje):
    while True:
        try:
            dato = float(input(mensaje))
            break  # Salir del bucle si la entrada es un número válido
        except ValueError:
            print("Dato invalido. Por favor, ingresa un número.")
        # Aquí continúa el código después de haber obtenido un número válido.
    return dato

# Función para agregar un nuevo articulo a la lista 'articulos'.
def altaArticulos(articulos, unidades, proveedores, articulosT):
    import clases.claseTipoUnidad    
    import clases.claseProveedores    
    import clases.claseTipoArticulos    

    menClaveArticulo = "Dame la clave del articulo: "
    auxClaveArticulo = 0
    auxClaveArticulo = get_datoI(menClaveArticulo)

    auxDescripcion=input("Dame el descripcion del articulo: ")

    menCosto = "Dame el costo del articulo: "
    auxCosto = 0
    auxCosto = get_datoF(menCosto)

    menPrecioMayoreo = "Dame el PrecioMayoreo del articulo: "
    auxPrecioMayoreo = 0
    auxPrecioMayoreo = get_datoF(menPrecioMayoreo)

    menPrecioMenudeo = "Dame la precioMenudeo del articulo: "
    auxPrecioMenudeo = 0
    auxPrecioMenudeo = get_datoF(menPrecioMenudeo)

    menExistenciaAlmacen = "Dame la existenciaAlmacen del articulo: "
    auxExistenciaAlmacen = 0
    auxExistenciaAlmacen = get_datoI(menExistenciaAlmacen)

    menExistenciaPisoVenta = "Dame la existenciaPisoVenta del articulo: "
    auxExistenciaPisoVenta = 0
    auxExistenciaPisoVenta = get_datoI(menExistenciaPisoVenta)

    clases.claseTipoUnidad.imprimirTipounidades(unidades)
    menCveTipoUnidad = "Dame la existenciaPisoVenta del articulo: "
    auxCveTipoUnidad = 0
    auxCveTipoUnidad = get_datoI(menCveTipoUnidad)
    while(clases.claseTipoUnidad.buscarTipoUnidad(auxCveTipoUnidad, unidades) == -1):
        print("La clave no existe")
        auxCveTipoUnidad = get_datoI(menCveTipoUnidad)

    clases.claseProveedores.imprimirProveedor(proveedores)
    menCveProveedor = "Dame la clave del proveedor: "
    auxCveProveedor = 0
    auxCveProveedor = get_datoI(menCveProveedor)
    while(clases.claseProveedores.buscarProveedor(auxCveProveedor, proveedores) == -1):
        print("La clave no existe")
        auxCveProveedor = get_datoI(menCveProveedor)

    clases.claseTipoArticulos.imprimirTipoArticulos(articulosT)
    menCveTipoArticulo = "Dame la clave del tipo del articulo: "
    auxCveTipoArticulo = 0
    auxCveTipoArticulo = get_datoI(menCveTipoArticulo)
    while(clases.claseTipoArticulos.buscarTipoArticulo(auxCveTipoArticulo, articulosT) == -1):
        print("La clave no existe")
        auxCveTipoArticulo = get_datoI(menCveTipoArticulo)

    # Agregamos los datos de las auxiliares de cada campo a la lista de articulos 
    articulos.append(articulo(auxClaveArticulo, auxDescripcion, auxCosto, auxPrecioMayoreo, auxPrecioMenudeo, auxExistenciaAlmacen, auxExistenciaPisoVenta,auxCveProveedor, auxCveTipoUnidad, auxCveTipoArticulo))

    return articulos

# Función para imprimir una tabla con los datos de los articulos.
def impArticulos(articulos):
    # Imprimir encabezados de la tabla.
    print("\nTabla de articulos\n")
    print("-" * 118)
    print("|{:<6}|{:<20}|{:<6}|{:<12}|{:<12}|{:<10}|{:<14}|{:<9}|{:<9}|{:<9}|".format(
        "Clave", "Descripción", "Costo", "Pre.Mayoreo", "Pre.Menudeo", "Exi.Almcen", "Exi.PisoVenta", "CveTipoU", "CvePro.","claveT"))
    print("-" * 118)

    # Imprimir los datos de cada articulo en filas.
    for ind in range(0,len(articulos),1):
        print(f"|{articulos[ind].getClaveArticulo():<6}|{articulos[ind].getDescripcion():<20}|{articulos[ind].getCosto():<6}|{articulos[ind].getPrecioMayoreo():<12}|{articulos[ind].getPrecioMenudeo():<12}|{articulos[ind].getExistenciaAlmacen():<10}|{articulos[ind].getExistenciaPisoVenta():<14}|{articulos[ind].getClaveTipoUnidad():<9}|{articulos[ind].getClaveProveedor():<9}|{articulos[ind].getClaveTipoArticulo():<9}|")
        print("-" * 118)

    print("")

def buscaArticulos(auxClaveArticulo,articulos):
   #Cremos una variante "indice" en -1
    indice=-1

    #Iera sobre los indices de la lista "articulos", para despues comprobar si la clave coincide con el en la posicion, en caso de no encontralo indice sera -1
    for ind in range (0, len(articulos), 1):
        if (articulos[ind].getClaveArticulo()==auxClaveArticulo):
            indice=ind
    return indice

# Pide la clave de el articulo aplicando el codigo de bucaArticulos para despues actulizar los valores de la lista si no se encuentre saltara un mensajes de que no se a encontrado
def modificaArticulo(articulos, unidades, proveedores, articulosT):
    import clases.claseTipoUnidad    
    import clases.claseProveedores    
    import clases.claseTipoArticulos  

    impArticulos(articulos)

    menClaveArticulo = "Numero de control " + str(articulos[ind].getClaveArticulo()) + "<- " 
    modClaveArticulo = 0
    modClaveArticulo = get_datoI(menClaveArticulo)
    ind=buscaArticulos(modClaveArticulo,articulos)

    if (ind!=-1):

        menClaveArticulo = "Dame la clave " + str(articulos[ind].getClaveArticulo()) + "<- " 
        auxClaveArticulo = 0
        auxClaveArticulo = get_datoI(menClaveArticulo)

        auxDescripcion=input("Descripcion " + str(articulos[ind].getDescripcion()) + "<- " )

        menCosto = "Costo " + str(articulos[ind].getCosto()) + "<- " 
        auxCosto = 0
        auxCosto = get_datoF(menCosto)
        
        menPrecioMayoreo = "Presio Mayoreo " + str(articulos[ind].getPrecioMayoreo()) + "<- " 
        auxPrecioMayoreo = 0
        auxPrecioMayoreo = get_datoF(menPrecioMayoreo)
        
        menPrecioMenudeo = "precio Menudeo " + str(articulos[ind].getPrecioMenudeo()) + "<- " 
        auxPrecioMenudeo = 0
        auxPrecioMenudeo = get_datoF(menPrecioMenudeo)
        
        menExistenciaAlmacen = "Existencia almacen " + str(articulos[ind].getExistenciaAlmacen()) + "<- "  
        auxExistenciaAlmacen = 0
        auxExistenciaAlmacen = get_datoI(menExistenciaAlmacen)
        
        menExistenciaPisoVenta = "Pxistencia piso venta " + str(articulos[ind].getExistenciaPisoVenta()) + "<- " 
        auxExistenciaPisoVenta = 0
        auxExistenciaPisoVenta = get_datoI(menExistenciaPisoVenta)

        clases.claseTipoUnidad.imprimirTipounidades(unidades)
        menCveTipoUnidad = "Dame la clave de la unidad del articulo " + str(articulos[ind].getClaveTipoUnidad()) + "<- " 
        auxCveTipoUnidad = 0
        auxCveTipoUnidad = get_datoI(menCveTipoUnidad)
        while(clases.claseTipoUnidad.buscarTipoUnidad(auxCveTipoUnidad, unidades) == -1):
            print("La clave no existe")
            auxCveTipoUnidad = get_datoI(menCveTipoUnidad)

        clases.claseProveedores.imprimirProveedor(proveedores)
        menCveProveedor = "Dame la clave del proveedor " + str(articulos[ind].getClaveProveedor()) + "<- " 
        auxCveProveedor = 0
        auxCveProveedor = get_datoI(menCveProveedor)
        while(clases.claseProveedores.buscarProveedor(auxCveProveedor, proveedores) == -1):
            print("La clave no existe")
            auxCveProveedor = get_datoI(menCveProveedor)

        clases.claseTipoArticulos.imprimirTipoArticulos(articulosT)
        menCveTipoArticulo = "Dame la clave del tipo del articulo " + str(articulos[ind].getClaveTipoArticulo()) + "<- " 
        auxCveTipoArticulo = 0
        auxCveTipoArticulo = get_datoI(menCveTipoArticulo)
        while(clases.claseTipoArticulos.buscarTipoArticulo(auxCveTipoArticulo, articulosT) == -1):
            print("La clave no existe")
            auxCveTipoArticulo = get_datoI(menCveTipoArticulo)

        articulos[ind].setClaveArticulo(auxClaveArticulo)
        articulos[ind].setDescripcion(auxDescripcion)
        articulos[ind].setCosto(auxCosto)
        articulos[ind].setPrecioMayoreo(auxPrecioMayoreo)
        articulos[ind].setPrecioMenudeo(auxPrecioMenudeo)
        articulos[ind].setExistenciaAlmacen(auxExistenciaAlmacen)
        articulos[ind].setExistenciaPisoVenta(auxExistenciaPisoVenta)
        articulos[ind].setCveTipoUnidad(auxCveTipoUnidad)
        articulos[ind].setCveProveedor(auxCveProveedor)
        articulos[ind].setCveTipoArticulo(auxCveTipoArticulo)
        
    else:
        print("El número de control no existe")

    return articulos
    
def borrarArticulo(articulos):

    impArticulos(articulos)

    menClaveArticulo = "Dame la clave del articulo: "
    modClaveArticulo = 0
    modClaveArticulo = get_datoI(menClaveArticulo)
    
    # Busca el articulo
    indice = buscaArticulos(modClaveArticulo, articulos)

    if indice != -1:
        # Eliminar los datos del articulo de la lista
        del articulos[indice]
    else:
        print("El número de control no existe")
    
    return articulos