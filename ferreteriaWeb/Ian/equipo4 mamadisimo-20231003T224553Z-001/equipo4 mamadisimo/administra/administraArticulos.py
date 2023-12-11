#se hace la importacion del modulo de la clase de articulos 
from clases.claseArticulo import *
# importacion del los modulos de administra de tipo proveedore, unidad y articulos
from administra.administraTipoArticulos import *
from administra.administraTipoUnidad import *
from administra.administraTipoProveedor import *


# Vamos a pedirle al usurio los datos de los articulos hasta que ya no quiere continuar en la lista que le corresponda
#definimos lo de adm Articulos el de tipo articulos unidades 
def admArticulos(articulos, unidades, proveedores, articulosT):
    #le agregamos la opcion para cuando le preguntemos al usiario nos puede decir que no o si 
    opcion ="N"
    #agregamos un while para que se pueda hacer un ciclo 
    while opcion!="S":
        #imprimimos los botones 
        print("")
        print("Menu de articulos")
        print("")
        print("[A]lta de articulos")
        print("[M]odificar un articulo")
        print("[B]orra un articulo")
        print("[I]prime listado de articulos")
        print("\nTipos\n")
        print("[U]nidad")
        print("[T]ipo articulos")
        print("")
        print("[S]salir")
        print("")
        #esta opcion es para obtener la eleccion que iso el usiario 
        opcion=input("Opción: ").upper()
        #se pone las funciones dependiendo de la opcion que alla elegido el usiario 
        print("")
        if opcion == "A":
            #estas funciones son para que puedan funcionar los votones 
            articulos=altaArticulos(articulos, unidades, proveedores, articulosT)

        elif opcion =="M":
            articulos=modificaArticulo(articulos, unidades, proveedores, articulosT)

        elif opcion =="B":
            articulos=borrarArticulo(articulos)
        
        elif opcion =="I":
            impArticulos(articulos)

        elif opcion =="U":
            unidades=admTipoUnidad(unidades)

        elif opcion =="T":
            articulosT=admTipoArticulo(articulosT)
        #opcion para salir al menu principal 
        elif opcion == "S":
            print("Volviendo al menu")
            #se agrega el return para que devuelva los valores que se mencionan
            return articulos, unidades, proveedores, articulosT
        #por ultimo se agrega un mensaje por si la opcion no se encuentra o no es valida 
        else:
            print("Opción invalida")    