'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

edad =int(input("Dime tu edad: "))

if edad > 0:
    if edad >= 0 and edad <=12 :
        print("Niño")
        
    elif edad >= 13 and edad <=17 :
        print("Adolescente")
        
    elif edad >= 18 and edad <= 29 :
        print("Joven")
    
    elif edad >= 100 :
        print("Edad errónea") 
    
    else: 
        print("Adulto")
else:
    print("Edad errónea")