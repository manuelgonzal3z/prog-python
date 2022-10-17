'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

numero1 = int(input("Inserta un número: "))
numero2 = int(input("Inserta un número: "))
distancia = numero1 - numero2

if distancia > 0:
    print(distancia)
elif distancia < 0:
    print(distancia * -1)