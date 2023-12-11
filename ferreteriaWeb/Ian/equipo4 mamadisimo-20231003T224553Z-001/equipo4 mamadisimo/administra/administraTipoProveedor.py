#se hace la importacion del modulo de la clase del tipo proveedor
from clases.claseTipoProveedor import *
#definimos el tipo proveedores
def admTipoProveedor(proveedoresT):
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si
    opcion="N"
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!="S":
        #imprimimos los botones
        print("")
        print("Menu de tipo proveedor")
        print("")
        print("[A]lta de el tipo de proveedor")
        print("[M]odificar el tipo de proveedor")
        print("[B]orra el tipo de proveedor")
        print("[I]prime listado de los tipos de proveedoresT")
        print("")
        print("[S]alir")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion == "A":
           #estas funciones son para que puedan funcionar los votones 
           proveedoresT = altaTipoProveedor(proveedoresT)    
        elif opcion =="M":
            proveedoresT = modificarTipoProveedor(proveedoresT)
        elif opcion =="B":
            proveedoresT = borrarTipoProveedores(proveedoresT)
        elif opcion =="I":
            imprimirTipoProveedores(proveedoresT)

        elif opcion == "S":
             #opcion para salir al menu principal
            print("Volviendo al menu de proveedores")
            #se agrega el return para que devuelva los valores que se mencionan
            return proveedoresT
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida
        else:
            print("Opción invalida")    
