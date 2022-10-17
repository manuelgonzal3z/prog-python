'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

estadoCivil = str(input("Introduzca su estado civil (S/D/C/V): "))
edad = int(input("Introduzca su edad: "))

estadoCivil1 = "S"
estadoCivil2 = "D"
estadoCivil3 = "C"
estadoCivil4 = "V"
if estadoCivil == (estadoCivil1 or estadoCivil2 or estadoCivil3 or estadoCivil4) and edad > 50:
    print("Se le debe aplicar una retención del 8.5%")
else:
    if estadoCivil == (estadoCivil1 and (edad > 0 and edad < 50)) or (estadoCivil2 and (edad > 0 and edad < 35)):
        print("Se le debe aplicar una retención del 12%")
    else:
        if estadoCivil == (estadoCivil4 and (edad > 0 and edad <50)) or (estadoCivil3 and (edad > 0 and edad < 35)):
            print("Se le debe aplicar una retención del 11.3%")
        else:
            print("Se le debe aplicar una retención del 10.5%")