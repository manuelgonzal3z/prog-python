'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

pago = 10
suma = pago
contador = 1

while contador < 21:
    print(f'El pago del mes {contador} es de {pago} €')
    pago*=2
#    contador+=1
    suma+=pago
    
print(f'El precio total ha sido de {suma//2} €')
