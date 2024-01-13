import os
from manejoErrores import *
import json
movie = "peliculas.json"

def crearPeliculas(peliculas,genero,actores):
        while True:
            with open(movie,'r') as archivo:
                peliculas=json.load(archivo)
            contP = len(peliculas)
            codigo = f"P0{contP+1}"
            os.system('cls')
            print("Ingrese el nombre de la pelicula (sin espacios):")
            nombre = letras()
            print("Ingrese la duracion:\ncantidad de horas:")
            hora = manejoEnteros()
            print("minutos:")
            minutos = manejoEnteros()
            print("Segundos:")
            segundos = manejoEnteros()
            duracion = str(f"{hora}:{minutos}:{segundos}")
            actorTemporal = {}                
            while True:
                print("Ingrese el nombre del actor:\n(Sin espacios y la primera letra en mayuscula ejemplo: PepitoPerez)")
                nombreActor = letras()
                for id in actores:
                    if nombreActor in actores[id].values():
                        print("Selecione el rol:\n\t1.Principal\n\t2.Antagonista\n\t3.Reparto")
                        selec = manejoEnteros()                  
                        rol = actores[id]['rol'][selec-1]
                        actorTemporal[id]={'nombre':nombreActor,
                                           'rol':rol}
                        bandera1 = True
                        
                    else:
                        print("Actor no existe\nEnter para continuar")
                        input()
                            
                print("desea agregar otro actor?:\n\t1. Si \n\t2. no")
                selec = manejoEnteros()
                if selec == 1: continue
                elif selec == 2:break
                else: break
            print("Ingresa el nombre del genero")
            generoP = letras()
            for clave in genero:
                if generoP == genero[clave]['nombre']:
                    generoP = genero[clave]
                    bandera = True
                else:
                    print("Genero no existe\nEnter para continuar")
                    input()
            if bandera and bandera1:
                peliculas[codigo]={'nombre':nombre,
                                        'genero':generoP,
                                        'duracion':duracion,
                                        'actores':actorTemporal                                          
                                        }
            else: print("Falta informacion, no se ha guardado")
            print("desea agregar otra pelicula?:\n\t1. Si \n\t2. no")
            with open(movie,'w+') as archivo2:
                json.dump(peliculas,archivo2,indent=4)
            selec = manejoEnteros()
            if selec == 1: continue
            elif selec == 2:break
            else: print("Ingrese 1 o 2")
            print(peliculas)
            input("Preciona Enter")
        
        

 
def editarPeliculas(peliculas):
    while True:
        os.system('cls')
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
    with open(movie,'w+') as archivo2:
            json.dump(peliculas,archivo2,indent=4)
    
def eliminarPelicula(peliculas):
    while True:
        os.system('cls')
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
    with open(movie,'w+') as archivo2:
            json.dump(peliculas,archivo2,indent=4)
