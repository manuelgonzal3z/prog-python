'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

mes = int(input("Introduce el mes de forma numérica: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("El mes indicado tiene 31 días")
elif mes == 2:
    print("El mes indicado tiene 28 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes indicado tiene 30 días")
else:
    print("Los datos introducidos no son correctos")
