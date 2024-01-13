import os
from manejoErrores import*
#from main import *
import json

def crearGenero(generos):
    
    
    while True:
        with open('generos.json','r') as archivo:
            generos=json.load(archivo)
        contG=len(generos)
        os.system("cls")
        print("ingresa el nombre del genero:\n(sin espacios)")
        nombregenero=letras()
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