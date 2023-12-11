#se hace la importacion del modulo de la clases clientes
from clases.claseCliente  import *
#importacion del los modulos de administra tipo cliente 
from administra.administraTipoCliente import *
#definimos lo de adm clientes y el de tipo clientes 
def admClientes(clientes, clientesT):
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si 
    opcion="N"
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!="S":
        #imprimimos los botones 
        print("")
        print("Menu de clientes")
        print("")
        print("[A]lta de clientes")
        print("[M]odificar un cliente")
        print("[B]orra un cliente")
        print("[I]prime listado de clientes")
        print("")
        print("[T]ipo de clientes")
        print("")
        print("[S]alir")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario 
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion == "A":
            #estas funciones son para que puedan funcionar los votones 
           clientes = altaCliente(clientes, clientesT)    

        elif opcion =="M":
            clientes = modificarCliente(clientes, clientesT)

        elif opcion =="B":
            clientes = borrarCliente(clientes)

        elif opcion =="I":
            imprimirTabla(clientes)

        elif opcion =="T":
            clientesT = admTipoClientes(clientesT)

        elif opcion == "S":
            #opcion para salir al menu principal 
            print("Volviendo al menu")
            #se agrega el return para que devuelva los valores que se mencionan
            return clientes, clientesT
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida 
        else:
            print("Opción invalida")    
