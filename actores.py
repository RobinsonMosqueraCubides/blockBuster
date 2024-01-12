import os
import json
def crearActor(actores):
    contActor = len(actores)
    while True:
        os.system('clear')
        print("Ingrese el nombre del actor:\n(Sin espacios y con la primera mayusculas ejemplo PepitoPerez)")
        nombre = input("")      
        contActor+=1
        codigoActor = f"Ac0{contActor}"
        actores[codigoActor] = {'nombre':nombre,
                                'rol':('Protagonista','Antagonista','Reparto')               
                } 
        print("desea agregar otro actor?:\n\t1. Si \n\t2. no")
        selec = int(input(""))
        if selec == 1: continue
        elif selec == 2:break
        else: break
    with open('actores.json','w+') as archivo2:
        json.dump(actores,archivo2,indent=4)
    
