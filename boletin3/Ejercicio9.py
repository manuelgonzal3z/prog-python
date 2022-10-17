'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

producto = str(input("Inserta el tipo de producto (a/b/c): ")) 
precioOriginal = int(input("y el precio original del producto "))

if producto == "a":
    print("El precio del producto aplicando el descuento es de", precioOriginal - ((precioOriginal * 7)/100), "€")
elif producto == "c" or precioOriginal < 500:
    print("El precio del producto aplicando el descuento es de", precioOriginal - ((precioOriginal * 12)/100), "€")
elif producto == ("b" and precioOriginal >= 500) or precioOriginal >= 500:
    print("El precio del producto aplicando el descuento es de", precioOriginal - ((precioOriginal * 9)/100), "€")