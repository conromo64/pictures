#se hace la importacion del modulo de la clase del tipo unidad 
from clases.claseTipoUnidad import *
#definimos el tipo unidades 
def admTipoUnidad(unidades):
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si
    opcion="N"
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!="S":
        #imprimimos los botones
        print("")
        print("Menu de tipo unidades")
        print("")
        print("[A]lta de el tipo de la unidades ")
        print("[M]odificar el tipo de la unidades ")
        print("[B]orra el tipo de unidades ")
        print("[I]prime listado de los tipos de unidades ")
        print("")
        print("[S]alir ")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion == "A":
           #estas funciones son para que puedan funcionar los votones 
           unidades = altaTipoUnidad(unidades)    
        elif opcion =="M":
            unidades = modificarTipoUnidad(unidades)
        elif opcion =="B":
            unidades =borrarTipounidades(unidades)
        elif opcion =="I":
            imprimirTipounidades(unidades)

        elif opcion == "S":
            #opcion para salir al menu principal
            print("Volviendo al menu de proveedores")
            #se agrega el return para que devuelva los valores que se mencionan
            return unidades
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida
        else:
            print("Opción invalida")    
