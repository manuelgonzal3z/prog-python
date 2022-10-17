'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

limiteInferior = int(input('Inserta el límite inferior del intervalo: '))
limiteSuperior = int(input('Inserta el límite superior del intervalo: '))

while limiteInferior > limiteSuperior:
    limiteInferior = int(input('Inserta el límite inferior del intervalo: '))
    limiteSuperior = int(input('Inserta el límite superior del intervalo: '))

numero = int(input(f'Inserta un número entre {limiteInferior} y {limiteSuperior}: '))

suma = 0
fuera = 0
igual = 0

while numero != 0:
    
    numero = int(input(f'Inserta un número entre {limiteInferior} y {limiteSuperior}: '))
    if limiteInferior < numero < limiteSuperior:
        suma+=numero
    elif numero < limiteInferior or numero > limiteSuperior:
        fuera+=1
    else:
        igual+=1
    numero = int(input(f'Introduzca un número entre {limiteInferior} y {limiteSuperior}: '))

print(f'La suma de los números del intervalo es {suma}, fuera del intervalo hay {fuera} números')
print(f'Existen {igual} números que coinciden con los límites del intervalo')
