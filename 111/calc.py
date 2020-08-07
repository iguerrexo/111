"""
Program: Simple Calculator
Author: Nora Guerrero 

"""

#Global Vars

#Functions
def print_separator():
    print("_" * 35)

def print_menu():
    print_separator()
    print(' Python Calc ')
    print_separator()

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] divide")
    print("[x] Exit")

    print_separator()

def clear():    
#direct instructions
#Clear the terminal with python is the homework
import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(2)
# Ubuntu version 10.10
os.system('clear')


    print ('\n\n\n')


opc=''

while(opc != 'x'):
    print_menu()

    opc = input("Please Chose an option: ")

    if(opc == 'x'):
        break

    num1 = float(input("Provide num 1: "))
    num2 = float(input("Provide num 2: "))

    if(opc == '1'):
        print(num1 + num2)
    elif(opc =='2'):
        print(num1 - num2)
    elif(opc =='3'):
        print(num1 * num2)
    elif(opc =='4'):
        if(num2 == 0):
            print("Error, zero division not allowed")
        else:
            print(num1 / num2)
    else: 
        print("Please chose a valid option")

    input("press enter to continue")

print('Good Bye!!')

