import os
from manejoErrores import *
def busquedaCodigo(peliculas):
    os.system('cls')
    print("ID\tNombre")
    for id in peliculas:
        print(f"{id}\t{peliculas[id]['nombre']}")
    print("Ingrese el codigo de la pelicula:")
    id = input("")
    if id in peliculas:
        os.system('cls')
        print("ID\t|\tNombre\t|\tGenero\t|\tDuracion\t|") 
        print(f"{id}\t|\t{peliculas[id]['nombre']}\t|\t{peliculas[id]['genero']['nombre']}\t|\t{peliculas[id]['duracion']} \t|")
        input()
    else:
        print("pelicula no existe")
        input()
        busquedaCodigo()

def busqueraNombre(peliculas):
    os.system('cls')
    print("ID\tNombre")
    for id in peliculas:
        print(f"{id}\t{peliculas[id]['nombre']}")
    print("Ingrese el nombre de la pelicula:")
    id = letras()
    for codigo in peliculas:
        if id in peliculas[codigo].values():
            os.system('cls')
            print("ID\t|\tNombre\t|\tGenero\t|\tDuracion\t|") 
            print(f"{codigo}\t|\t{peliculas[codigo]['nombre']}\t|\t{peliculas[id]['genero']['nombre']}\t|\t{peliculas[codigo]['duracion']} \t|")
            input()

def listarPeliculas(peliculas):
    os.system('cls')
    print("|\t ID \t|\t Nombre \t|")
    for clave in peliculas:
        print(f"|\t {clave} \t|\t {peliculas[clave]['nombre']} \t|")
    print("Enter para continuar")
    input()    
    

