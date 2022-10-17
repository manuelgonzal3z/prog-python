'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

dia = str.upper(input("Indica qué día es (L/M/X/J/V/S/D): "))
turno = str.upper(input("Indica en qué turno has realizado la llamada (Mañana/Tarde): "))
tiempo = int(input("Indica cuántos minutos ha durado la llamada: "))

if tiempo >= 1 and tiempo <= 5:
    if dia == "D" and turno == "MAÑANA" or turno == "TARDE":
        print("La cantidad a pagar es:", (tiempo*1) + ((tiempo*1) * 0.03))
    elif dia == "L" or dia == "M" or dia == "X" or dia == "J" or dia == "V" or dia == "S":
        if turno == "MAÑANA":
            print("La cantidad a pagar es:", (tiempo*1) + ((tiempo*1) * 0.15))
        elif turno == "TARDE":
            print("La cantidad a pagar es:", (tiempo*1) + ((tiempo*1) * 0.10))
        else:
            print("Los datos introducidos no son correctos")
elif tiempo > 5 and tiempo <= 8:
    if dia == "D" and turno == "MAÑANA" or turno == "TARDE":
        print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 5) * 0.8)) + ((tiempo * 1) + ((tiempo - 5) * 0.8)) * 0.03)
    elif dia == "L" or dia == "M" or dia == "X" or dia == "J" or dia == "V" or dia == "S":
        if turno == "MAÑANA":
            print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 5) * 0.8)) + ((tiempo * 1) + ((tiempo - 5) * 0.8)) * 0.15)
        elif turno == "TARDE":
            print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 5) * 0.8)) + ((tiempo * 1) + ((tiempo - 5) * 0.8)) * 0.10)
        else:
            print("Los datos introducidos no son correctos")        
elif tiempo > 8 and tiempo <= 10:
    if dia == "D" and turno == "MAÑANA" or turno == "TARDE":
        print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 8) * 0.7)) + ((tiempo * 1) + ((tiempo - 8) * 0.7)) * 0.03)
    elif dia == "L" or dia == "M" or dia == "X" or dia == "J" or dia == "V" or dia == "S":
        if turno == "MAÑANA":
            print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 8) * 0.7)) + ((tiempo * 1) + ((tiempo - 8) * 0.7)) * 0.15)
        elif turno == "TARDE":
            print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 8) * 0.7)) + ((tiempo * 1) + ((tiempo - 8) * 0.7)) * 0.10)
        else:
            print("Los datos introducidos no son correctos")
elif tiempo > 10:
    if dia == "D" and turno == "MAÑANA" or turno == "TARDE":
        print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 10) * 0.5)) + ((tiempo * 1) + ((tiempo - 10) * 0.5)) * 0.03)
    elif dia == "L" or dia == "M" or dia == "X" or dia == "J" or dia == "V" or dia == "S":
        if turno == "MAÑANA":
            print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 10) * 0.5)) + ((tiempo * 1) + ((tiempo - 10) * 0.5)) * 0.15)
        elif turno == "TARDE":
            print("La cantidad a pagar es:", ((tiempo * 1) + ((tiempo - 10) * 0.5)) + ((tiempo * 1) + ((tiempo - 10) * 0.5)) * 0.10)
        else:
            print("Los datos introducidos no son correctos")