'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

año = int(input("Indique el año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año introducido es año bisiesto")
        else:
            print("El año introducido no es año bisiesto")