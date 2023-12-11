#se hace la importacion del modulo de la clase del tipo cliente 
from clases.claseTipoCliente import *
#definimos el tipo clientes
def admTipoClientes(clientesT):
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si
    opcion="N"
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!="S":
        #imprimimos los botones 
        print("")
        print("Menu de tipo clientes")
        print("")
        print("[A]lta de el tipo de cliente")
        print("[M]odificar el tipo de cliente")
        print("[B]orra el tipo de cliente")
        print("[I]prime listado de los tipos de cliente")
        print("")
        print("[S]alir")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion == "A":
            #estas funciones son para que puedan funcionar los votones 
            clientesT =  altaTipoCliente(clientesT)    
        elif opcion =="M":
            clientesT =  modificarTipoClientes(clientesT)
        elif opcion =="B":
            clientesT = borrarTipoClientes(clientesT)
        elif opcion =="I":
            imprimirTipoClientes(clientesT)

        elif opcion == "S":
             #opcion para salir al menu principal
            print("Volviendo al menu de clientes")
            #se agrega el return para que devuelva los valores que se mencionan
            return clientesT
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida
        else:
            print("Opción invalida")    
