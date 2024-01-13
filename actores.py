import os
import json
from manejoErrores import *
def crearActor(actores):
    
    while True:
        with open('actores.json','r') as archivo:
            actores=json.load(archivo)
        contActor = len(actores)
        os.system('cls')
        print("Ingrese el nombre del actor:\n(Sin espacios y con la primera mayusculas ejemplo PepitoPerez)")
        nombre = letras()      
        contActor+=1
        codigoActor = f"Ac0{contActor}"
        actores[codigoActor] = {'nombre':nombre,
                                'rol':('Protagonista','Antagonista','Reparto')               
                } 
        print("desea agregar otro actor?:\n\t1. Si \n\t2. no")
        selec = int(input(""))
        with open('actores.json','w+') as archivo2:
            json.dump(actores,archivo2,indent=4)
        if selec == 1: continue
        elif selec == 2:break
        else: break
    

def eliminarActor(actores):
    while True:
        os.system('cls')
        print("Ingresa el codigo del actor")
        codigo = input("")    
        if codigo in actores:
            print(f"Deseas elminar a {actores[codigo]['nombre']}?\n\t1. Si \n\t2. No")
            selec = int(input(""))
            if selec == 1:
                actores[codigo] = {}
            else: continue
        print("desea eliminar otro actor?:\n\t1. Si \n\t2. no")
        selec = int(input(""))
        if selec == 1: continue
        elif selec == 2:break
        else: break
    with open('actores.json','w+') as archivo2:
        json.dump(actores,archivo2,indent=4) 


def listarActores(actores):
    os.system('cls')
    print("|\t ID \t|\t Nombre \t|")
    for clave in actores:
        print(f"|\t {clave} \t|\t {actores[clave]['nombre']} \t|")
    print("Enter para continuar")
    input()    
