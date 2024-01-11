import os
from manejoErrores import *
#import json
#movie = "peliculas.json"
#contadore1 = "contadores1.json"
#dict={}
#contador = []
    
#with open(movie,'r') as archivo:
#        dict=json.load(archivo)
#with open(contadore1,'r') as archivo1:
#        contador=json.load(archivo1)

peliculas = {'A01': {'nombre': 'Robocot', 'genero': 'Accion', 'duracion': '2:36:24'}}
actores = {'Ac01': {'nombre': 'PepitoPerez', 'rol': ('Protagonista', 'Antagonista', 'Reparto')}}

def crearPeliculas()->str:

        conA=0
        conD=0
        conR=0
        while True:
            os.system('clear')
            print("Selecione el genero de la pelicula: \n\t1. Accion\n\t2. Drama\n\t3. Romance")
            selec = manejoEnteros()
            if selec ==1:
                genero = 'Accion'
                conA+=1
                codigo = str(f"A0{conA}")
            elif selec == 2:
                genero = 'Drama'
                conD+=1
                codigo = str(f"D0{conD}")
            elif selec == 3:
                genero = 'Romanace'
                conR+=1
                codigo = str(f"R0{conR}")
            else:
                print("Ingresa un numero del 1 al 3")
                input()
                continue
            print("Ingrese el nombre de la pelicula (sin espacios):")
            nombre = input("")
            print("Ingrese la duracion:\ncantidad de horas:")
            hora = manejoEnteros()
            print("minutos:")
            minutos = manejoEnteros()
            print("Segundos:")
            segundos = manejoEnteros()
            duracion = str(f"{hora}:{minutos}:{segundos}")
            while True:            
                print("Ingrese el nombre del actor:\n(Sin espacios y la primera letra en mayuscula ejemplo: PepitoPerez)")
                nombreActor = input("")
                for id in actores:
                    if nombreActor in actores[id].values():
                        print("Selecione el rol:\n\t1.Principal\n\t2.Antagonista\n\t3.Reparto")
                        selec = manejoEnteros()                  
                        rol = actores[id]['rol'][selec-1]
                        peliculas[codigo]={'nombre':nombre,
                                        'genero':genero,
                                        'duracion':duracion,
                                        'actores':{id:{'Nombre':nombreActor,
                                                        'rol':rol                                           
                                        }}}
                    else:
                        print("Actor no existe")
                        break
                print("desea agregar otro actor?:\n\t1. Si \n\t2. no")
                selec = manejoEnteros()
                if selec == 1: continue
                elif selec == 2:break
                else: print("Ingrese 1 o 2")
            print("desea agregar otra pelicula?:\n\t1. Si \n\t2. no")
            selec = manejoEnteros()
            if selec == 1: continue
            elif selec == 2:break
            else: print("Ingrese 1 o 2")
        print(peliculas)
        input("Preciona Enter")
#        contador1 = [conA,conD,conR]
        #lpelicula = [peliculas]
        
#        with open(movie,'w+') as archivo2:
#            json.dump(peliculas,archivo2,indent=4)
#        with open(contador,'w+') as archivo3:
#            json.dump(contador1,archivo3,indent=4)

 
def editarPeliculas():
    while True:
        os.system('clear')
        print("ingrese el codigo de la pelicula:")
        codigo = input("")
        if codigo in peliculas:
            print("Que deseas modificar:\n\t1. Nombre\n\t2. genero \n\t3. Duracion \n\t4. Actores")
            selec = manejoEnteros()
            if selec == 1:
                print("Ingrese el nombre de la pelicula (sin espacios):")
                nombre = input("")
                peliculas[codigo]['nombre'] = nombre
            elif selec == 2: 
                print("Selecione el genero de la pelicula: \n\t1. Accion\n\t2. Drama\n\t3. Romance")
                selec = manejoEnteros()
                if selec == 1: genero = 'Accion'
                elif selec == 2: genero = 'Drama'
                elif selec == 3: genero = 'Romance'
                else: genero = 'sin determinar'
                peliculas[codigo]['genero']=genero
            elif selec == 3:
                print("Ingrese la duracion:\ncantidad de horas:")
                hora = manejoEnteros()
                print("minutos:")
                minutos = manejoEnteros()
                print("Segundos:")
                segundos = manejoEnteros()
                peliculas[codigo]['duracion']=str(f"{hora}:{minutos}:{segundos}")
            else:
                print('ingrese un numero del 1 al 3')
                input()
                continue
        else:
            print("pelicula no existe")
            input()
            break
        print("desea editar otra pelicula?:\n\t1. Si \n\t2. no")
        selec = manejoEnteros()
        if selec == 1: continue
        elif selec == 2:break
        else: break
    
def eliminarPelicula():
    while True:
        os.system('clear')
        print('Ingrese el codigo de la pelicula')
        codigo = input("")
        if codigo in peliculas:
            print(f"Deseas elminar a {peliculas[codigo]['nombre']}?\n\t1. Si \n\t2. No")
            selec = int(input(""))
            if selec == 1:
                peliculas[codigo]={}
            elif selec == 2: break
            else: continue
        else:
            print("pelicula no existe")
            input()
            continue
        print("desea eliminar otra pelicula?:\n\t1. Si \n\t2. no")
        selec = int(input(""))
        if selec == 1: continue
        elif selec == 2:break
        else: break
    print(peliculas[codigo])
