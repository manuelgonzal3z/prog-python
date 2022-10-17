'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

print("Distancia entre los valores en un plano cartesiano")
x1 = int(input("Inserta un número (x1): "))
y1 = int(input("Inserta un número (y1): "))
x2 = int(input("Inserta un número (x2): "))
y2 = int(input("Inserta un número (y2): "))

distancia = ((((x2-x1)**2)+((y2-y1)**2))**0.5)

print(distancia)