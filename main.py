import os
from generos import*
from pelicuas import *
from busqueda import *
from manejoErrores import *
from actores import *
def menuPrincial():
        
    while True:
        with open(movie,'r') as archivo:
            peliculas=json.load(archivo)
        with open('generos.json','r') as archivo:
            generos=json.load(archivo)
        with open('actores.json','r') as archivo:
            actores=json.load(archivo)
        
        print("Selecion la accion:\n\t1. Busqueda de Peliculas\n\t2. Registro peliculas\n\t3. Registro actores\n\t4. Generos\n\t5. Salir")
        selec = manejoEnteros()
        if selec == 1:
            print("Selecion la accion:\n\t1. Busqueda por codigo\n\t2. Busqueda por nombre\n\t3. Menu anterior")
            selec = manejoEnteros()
            if selec == 1: busquedaCodigo(peliculas)
            elif selec == 2: busqueraNombre(peliculas)
            elif selec == 3: continue
        elif selec == 2:
            print("Selecione la accion:\n\t1. Registrar Pelicula\n\t2. Editar pelicula\n\t3. eliminar pelicula\n\t4. imprimir datos")
            select1 = manejoEnteros()
            if select1 == 1: crearPeliculas(peliculas,generos,actores)
            elif select1 == 2: editarPeliculas(peliculas)
            elif select1 == 3: eliminarPelicula(peliculas)
            elif select1 == 4: continue
        elif selec == 3: crearActor(actores)
        elif selec == 4: 
            print("Selecion la accion:\n\t1. Crear generos\n\t2. Listar Generos\n\t3. Menu anterior")
            selec = manejoEnteros()
            if selec == 1: crearGenero(generos)
            elif selec == 2: listarGeneros(generos)
            elif selec == 3: continue
        elif selec == 5: break
        else: continue
menuPrincial()
            