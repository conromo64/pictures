import manipluaJson
import administraArticulos
import administraTipoArticulo
import administraClientes
articulos = manipluaJson.leeJsonArticulos()
clientes = []
tipoArticulos = manipluaJson.leeJsonTipoArticulos()
##articulos = []
opcion = 'N'
while opcion!='S':
    print("[A]rticulos ")
    print("[C]lientes ")
    print("[T]ipo de Articulo")
    print("[S]alir")
    opcion=input().upper()
    if opcion=="A":
        articulos = administraArticulos.admArticulos(articulos,tipoArticulos)
    elif opcion=="C":
        clientes = administraClientes.admClientes(clientes)
    elif opcion=="T":
        clientes = administraTipoArticulo.admTipoArticulos(tipoArticulos)
    elif opcion=="S":
        manipluaJson.creaJsonArticulo(articulos)
        manipluaJson.creaJsonTipoArticulo(tipoArticulos)
        print("Adios")
    else:
        print("OPCION  INVALIDA!")     