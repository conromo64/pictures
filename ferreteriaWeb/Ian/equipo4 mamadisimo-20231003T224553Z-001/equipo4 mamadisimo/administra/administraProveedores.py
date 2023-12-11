#se hace la importacion del modulo de la clase proveedores
from clases.claseProveedores import *
#importacion del los modulos de administra tipo proveedor 
from administra.administraTipoProveedor import *
#definimos lo de adm proveedores y el de tipo proveedores
def amdminProveedor(proveedor, proveedoresT):
#esta funcion toma el papel de menu principal 
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si
    opcion ='n'
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!= 's':
        #imprimimos los botones 
        print("")
        print("Menu de proveedores")
        print("")
        print("[A]lta de proveedores")
        print("[I]mprime listedo de proveedores")
        print("[M]odifica un proveedores")
        print("[B]orra un proveedor")
        print("")
        print("[T]ipo proveedor")
        print("")
        print("[S]alir")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario 
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion=="A":
            #estas funciones son para que puedan funcionar los votones 
            proveedor = altaProveedor(proveedor, proveedoresT)

        elif opcion=="M":
            proveedor = modificarProveedor(proveedor, proveedoresT)

        elif opcion =="B":
            proveedor = borrarProveedor(proveedor)

        elif opcion=="I":
            imprimirProveedor(proveedor)

        elif opcion =="T":
            proveedoresT = admTipoProveedor(proveedoresT)

        elif opcion=="S":
            #opcion para salir al menu principal 
            print("Volviendo al menu")
            #se agrega el return para que devuelva los valores que se mencionan
            return proveedor, proveedoresT
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida 
        else:
            print("OPCION INVALIDA")