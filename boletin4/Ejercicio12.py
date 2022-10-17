'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

tipo = str.upper(input("Introduce el tipo (A/B): "))
tamaño = int(input("Introduce el tamaño (1/2)"))
precio = 90

if tipo == "A" and tamaño == 1:
    print("La ganancia obtenida es de", precio + 20, "centimos")
elif tipo == "A" and tamaño == 2:
    print("La ganancia obtenida es de", precio + 30, "centimos")
elif tipo == "B" and tamaño == 1:
    print("La ganancia obtenida es de", precio - 30, "centimos")
elif tipo == "B" and tamaño == 2:
    print("La ganancia obtenida es de", precio - 50, "centimos")
else:
    print("Los datos introducidos son incorrectos")
