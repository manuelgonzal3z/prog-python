'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

caracter = input("Inserta un caracter: ")
num1 = int(input("Inserta un número entero: "))
num2 = int(input("Inserta otro número entero: "))

if caracter == "+" :
    print(num1 + num2)
elif caracter == "-" :
    print(num1 - num2)
elif caracter == "*":
    print(num1 * num2)
elif caracter == "/":
    print(num1 / num2)
elif caracter == "%":
    print(num1 % num2)
else:
    print("El caracter introducido es incorrecto")