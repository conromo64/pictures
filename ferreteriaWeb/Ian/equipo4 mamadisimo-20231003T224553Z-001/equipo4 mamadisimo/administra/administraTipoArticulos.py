from clases.claseTipoArticulos import *

#definimos el tipo articulos 
def admTipoArticulo(articulosT):
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si
    opcion="N"
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!="S":
        #imprimimos los botones 
        print("")
        print("Menu de tipo articulos")
        print("")
        print("[A]lta de el tipo de articulos")
        print("[M]odificar el tipo de articulos")
        print("[B]orra el tipo de articulos")
        print("[I]prime listado de los tipos de articulos")
        print("")
        print("[S]alir")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario 
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion == "A":
            #estas funciones son para que puedan funcionar los votones 
            articulosT = altaTipoArticulos(articulosT)    

        elif opcion =="M":
            articulosT = modificarTipoArticulo(articulosT)

        elif opcion =="B":
            articulosT = borrarTipoArticulo(articulosT)
            
        elif opcion =="I":
            imprimirTipoArticulos(articulosT)

        elif opcion == "S":
            #opcion para salir al menu principal 
            print("Volviendo al menu de articulos")
            #se agrega el return para que devuelva los valores que se mencionan
            return articulosT
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida
        else:
            print("Opción invalida")    
