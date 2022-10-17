'''
Created on 14 oct 2022

@author: manuelGonzalez
'''

'''
Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format:
7*0=0
7*1=7
.....
7*10=70
'''

numero = int(input('Enter one number between 0 and 10: '))

if numero > 10 or numero < 0:
    print('The number is out of the boundaries')
else:
    for i in range(0, 11):
        print(f'{numero}*{i}={numero*i}')
        