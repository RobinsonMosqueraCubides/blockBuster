import os
from manejoErrores import*
def listarPeliculasGenero(peliculas):
    os.system('cls')
    print("Ingresa el nombre del genero")
    nombreGenero = letras()
    for clave in peliculas:
        if nombreGenero in peliculas[clave]['genero']['nombre']:
            print(f"|\t {peliculas[clave]['nombre']} \t|")
    print("Enter para continuar")
    input()
def listarPeliculasActor(peliculas):
    os.system('cls')
    print("Ingresa el nombre del actor")
    nombreActor = letras()
    for clave in peliculas:
        for claveActor in peliculas[clave]['actores']:
            if nombreActor in peliculas[clave]['actores'][claveActor].values():
                print(f"|\t {peliculas[clave]['nombre']} \t|\t {peliculas[clave]['actores'][claveActor]['rol']} \t|")
    print("Enter para continuar")
    input()