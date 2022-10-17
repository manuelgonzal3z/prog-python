'''
Created on 17 oct 2022

@author: manuelGonzalez
'''

e2 = int(input("Indica cuantas monedas de 2€ tienes: "))
e1 = int(input("Indica cuántas monedas de 1€ tienes: "))
cent50 = int(input("Indica cuántas monedas de 50 céntimos tienes: "))
cent20 = int(input("Indica cuántas monedas de 20 céntimos tienes: "))
cent10 = int(input("Indica cuántas monedas de 10 céntimos tienes: "))

cent_e2 = (e2*200)
cent_e1 = (e1*100)
cent_cent50 = (cent50*50)
cent_cent20 = (cent20*20)
cent_cent10 = (cent10*10)

print((cent_e2+cent_e1+cent_cent50+cent_cent20+cent10)//100, "€")