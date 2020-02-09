from calculator import *
import os
# import time
# time.sleep(3)


def header():
    print("Welcome to Calculatro!")
    print("======================")
    print("For calculation:")


header()

# Creation & Instantiation
menu = 0
cal = calculator(input("Enter 1st Value: "),
                 input("Enter 2nd Value: "))

# Processing
while(True):
    print("\n1.Addition\t2.Subtraction\n3.Multiplication\t")
    print("4.Division\n5.Print Last Result\t6.Change Values")
    print("7.Print Values\t8.Exit")

    menu = input("Choose on of above option: ")

    if(menu == "1"):
        cal.add()
    if(menu == "2"):
        cal.sub()
    if(menu == "3"):
        cal.mul()
    if(menu == "4"):
        cal.div()
    if(menu == "5"):
        cal.print()
    if(menu == "6"):
        cal.set_value1(input("Enter 1st value: "))
        cal.set_value2(input("Enter 2nd value: "))
    if(menu == "7"):
        cal.print_value()
    if(menu == "8"):
        break

    os.system("pause")
    os.system("cls")
