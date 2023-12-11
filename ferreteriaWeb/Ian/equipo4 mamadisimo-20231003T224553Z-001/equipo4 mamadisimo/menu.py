#Importa modulo manipulajson
from manipula.manipulaJson import *

#Importa funciones
from administra.administraArticulos import *
from administra.administraClientes import *
from administra.administraProveedores import *


# Utiliza las funciones para tranformar las linas json en objetos y almacernalas en listas
articulos = leeJsonArticulos()
articulosT = leeJsonTipoArticulo()
unidades = leeJsonTipoUnidad()

clientes = leeJsonClientes()
clientesT = leeJsonTipoClientes()

proveedores = leeJsonProveedor()
proveedoresT = leeJsonTipoProveedor()

# hace un menu usando la comparacion entre letras para segun la opcion habilite las funciones y listas para despues almacenarlas
opcion = "N"
while(opcion != "S"):

    print("")
    print("Menu")
    print("")
    print("[A]rticulos")
    print("[C]lientes")
    print("[P]rovedores")
    print("")
    print("[S]salir")
    print("")

    opcion = input("Opción: ").upper()

    if (opcion == "A"):
        articulos, unidades, proveedores, articulosT = admArticulos(articulos, unidades, proveedores, articulosT)

    elif (opcion == "C"):
        clientes, clientesT = admClientes(clientes, clientesT)

    elif (opcion == "P"):
        proveedor, proveedoresT = amdminProveedor(proveedores, proveedoresT)

    elif opcion =="S":
        creaJsonArticulo(articulos)
        creaJsonTipoArticulo(articulosT)
        creaJsonTipoUnidad(unidades)

        creaJsonCliente(clientes)
        creaJsonTipoClientes(clientesT)

        creaJsonProveedor(proveedores)
        creaJsonTipoProveedor(proveedoresT)

        print("Adios")
    else:
        print("OPCION INVALIDA!")