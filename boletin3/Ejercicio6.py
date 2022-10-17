'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

caracter = str(input("Inserta un caracter: "))

if caracter == "a" :
    print("Su caracter es una vocal")
    print("El caracter insertado es la primera vocal", caracter)

elif caracter == "e" :
    print("Su caracter es una vocal")
    print("El caracter insertado es la segunda vocal", caracter)
    
elif caracter == "i" :
    print("Su caracter es una vocal")
    print("El caracter insertado es la tercera vocal", caracter)    
    
elif caracter == "o" :
    print("Su caracter es una vocal")
    print("El caracter insertado es la cuarta vocal", caracter)
    
elif caracter == "u" :
    print("Su caracter es una vocal")
    print("El caracter insertado es la quinta vocal", caracter)    
    
elif caracter != "a" or caracter != "e" or caracter != "i" or caracter != "o" or caracter != "u" :
    print("Su caracter es una consonante")