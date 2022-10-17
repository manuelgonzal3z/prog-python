'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

base = int(input("Introduce la base de la potencia: "))
exponente = int(input("Introduce el exponente de la potencia: "))
potencia = base ** exponente

if exponente > 0:
    print("La solución de la potencia es", potencia)
elif exponente == 0:
    print("La solución de la potencia es 1")
elif exponente < 0:
    print("La solución de la potencia es", (potencia ** (exponente * -1)))