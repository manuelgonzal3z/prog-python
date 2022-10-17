'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

alumnos = int(input("Inserta el número de alumnos: "))
viaje = (4000 // alumnos)

if alumnos >= 100:
    print("El precio a pagar por persona sería", viaje + 65, "€")

elif alumnos >= 50 and alumnos <= 99:
    print("El precio a pagar por persona sería", viaje + 70, "€")
elif alumnos >= 30 and alumnos <= 49:
    print("El precio a pagar por persona sería", viaje + 95, "€")
elif alumnos < 30 and alumnos > 0:
    print("El precio a pagar por persona sería", viaje, "€")
else:
    print("Los datos introducidos son incorrectos")