import os
from manejoErrores import*
#from main import *
import json

def crearGenero(generos):
    
    contG=len(generos)
    while True:
        os.system("clear")
        print("ingresa el nombre del genero")
        nombregenero=input("")
        while True:
            for clave in generos:
                if nombregenero in generos[clave]['nombre']:                
                    print("Genero ya existe")
                else:
                    contG+=1
                    codigo = f'G0{contG}'
                    bandera = True
            break
        if bandera:
            generos[codigo]={'id':codigo,
                             'nombre':nombregenero}
            with open('generos.json','w+') as archivo2:
                json.dump(generos,archivo2,indent=4)   
            
              
                
        print("desea agregar otro genero?:\n\t1. Si \n\t2. no")
        selec = manejoEnteros()
        if selec == 1: continue
        elif selec == 2:break
        else: print("Ingrese 1 o 2")

def listarGeneros(generos):
    print("|\t ID \t|\t Nombre \t |")
    for i in generos:
        print(f"|\t {i} \t|\t {generos[i]['nombre']} \t |")
    print("Enter para continuar")
    input()