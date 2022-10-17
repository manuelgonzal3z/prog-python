'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

A = float(input("Indica la medida del lado A de tu triángulo: "))
B = float(input("Indica la medida del lado B de tu triángulo: "))
C = float(input("Indica la medida del lado C de tu triángulo: "))

if (A ** 2 + B ** 2 == C ** 2):
    print("Según las medidas introducidas, es un triángulo rectángulo")
elif (A == B and A == C):
    print("Según las medidas introducidas, es un triángulo equilátero")
elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
    print("Según las medidas introducidas, es un triángulo isósceles")
else:
    print("Según las medidas introducidas, es un triángulo escaleno")
