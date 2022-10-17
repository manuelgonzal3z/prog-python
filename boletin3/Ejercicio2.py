'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

num1 =int(input("Dime un número: "))
num2 =int(input("Dime otro número: "))

if num1 == num2 : 
    print("Ambos números son iguales")
    
elif num1 > num2 : 
    print("El primer número (%s) es mayor que el segundo (%s)" % (num1, num2))
    
elif num1 < num2 :
    print("El segundo número (%s) es mayor que el primero (%s)" % (num1, num2))
