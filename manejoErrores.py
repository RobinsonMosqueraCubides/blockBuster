def manejoEnteros():
    while True:
        try:
            x=float(input(""))
            return x
        except: print("Ingrese un numero")
def letras():
    while True:
        x = input("")
        if x.isalpha():
            return x
        else: print("Ingrese el nomre sin escpacios ni letras")