import os
from pelicuas import *
from busqueda import *
from manejoErrores import *
def menuPrincial():
    while True:
        print("Selecion la accion:\n\t1. Busqueda de Peliculas\n\t2. Registro peliculas\n\t3. Registro actores\n\t4. Salir")
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
            if select1 == 1: crearPeliculas()
            elif select1 == 2: editarPeliculas()
            elif select1 == 3: eliminarPelicula()
            elif select1 == 4: continue
        elif selec == 3: crearActor(actores)
        elif selec == 4: break
        else: continue
menuPrincial()
            