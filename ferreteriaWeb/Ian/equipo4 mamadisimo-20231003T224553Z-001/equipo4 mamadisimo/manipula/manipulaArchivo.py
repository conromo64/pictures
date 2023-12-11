# Abre el archivo que esta en la ruta
def leerArchivo(ruta):
    #Lee las lineas de el archivo
    with open(ruta,'r')as archivo:
        datos = [dato.rstrip('\n')for dato in archivo.readlines()]
    #Cierra el archivo
    archivo.close()
    return datos


def borraArchivo(ruta):
    # Importa la clase 'Path' del módulo 'pathlib'
    from pathlib import Path
    # Crea un objeto 'archivo' de la clase 'Path' utilizando la ruta
    archivo = Path(ruta)
    if archivo.is_file():
        #Si el archivo exite lo borra usando unlink
        archivo.unlink()
        print(f'El Archivo "{ruta}"ha sido borrado.')
    #no se encotro
    else:
        print(f'El Archivo "{ruta}"no existe')

def creaArchivo(ruta,datos):
    borraArchivo(ruta)
    # Abre el archivo en modo escritura ('w')
    with open (ruta, 'w')as archivo:
        #Itera en la lista
        for dato in datos:
            #escribe los datos
            archivo.write(dato+"\n")
    print(f"Se ha creado el archivo '{ruta}'con exito.\n")

