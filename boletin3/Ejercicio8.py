'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

h1 = 30
h2 = 11
m1 = 11
m2 = 11
s1 = 12
s2 =12

if 0<=h1 and 24>h1 and 0<=h2 and 24>h2 and 0<=m1 and 60>m1 and 0<=m2 and 60>m2 and 0<=s1 and 60>s1 and 0<=s2 and 60>s2:
    if h1 > h2 :
        print("Hora 1 es mayor que Hora 2")
    elif h1 < h2 :
        print("Hora 2 es mayor que Hora 1")
    else:
        if m1 > m2 :
            print("La hora 1 es mayor que la hora 2")
        elif m2 > m1 : 
            print("La hora 2 es mayor que la hora 1")
        else:
            if s1 > s2 :
                print("La hora 1 es mayor que la hora 2")
            elif s1 < s2 :
                print("La hora 2 es mayor que la hora 1")
            else:
                print("Ambas horas son iguales")
                    
else:
     print("Los datos introducidos son incorrectos")  