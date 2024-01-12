import os

def busquedaCodigo(peliculas):
    os.system('clear')
    print("ID\tNombre")
    for id in peliculas:
        print(f"{id}\t{peliculas[id]['nombre']}")
    print("Ingrese el codigo de la pelicula:")
    id = input("")
    if id in peliculas:
        os.system('clear')
        print("ID\t|\tNombre\t|\tGenero\t|\tDuracion\t|") 
        print(f"{id}\t|\t{peliculas[id]['nombre']}\t|\t{peliculas[id]['genero']}\t|\t{peliculas[id]['duracion']} \t|")
        input()
    else:
        print("pelicula no existe")
        input()
        busquedaCodigo()

def busqueraNombre(peliculas):
    os.system('clear')
    print("ID\tNombre")
    for id in peliculas:
        print(f"{id}\t{peliculas[id]['nombre']}")
    print("Ingrese el nombre de la pelicula:")
    id = input("")
    for codigo in peliculas:
        if id in peliculas[codigo].values():
            os.system('clear')
            print("ID\t|\tNombre\t|\tGenero\t|\tDuracion\t|") 
            print(f"{codigo}\t|\t{peliculas[codigo]['nombre']}\t|\t{peliculas[codigo]['genero']}\t|\t{peliculas[codigo]['duracion']} \t|")
            input()
    

