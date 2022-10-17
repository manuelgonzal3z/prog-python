'''
Created on 14 oct 2022

@author: manuelGonzalez
'''

'''
Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.
'''

contador = 1

while contador < 101:
    contador+=1
    if contador%7 == 0:
        print(f'The number {contador} is a multiple of 7')
    if contador%13 == 0:
        print(f'The number {contador} is a multiple of 13')
