from calculator import *

print("Welcome to Calculatro!")
print("======================")
print("\nFor calculation:")
menu = 0
while(menu != '8'):
    cal = calculator(input("Enter numbers: \n"),
                     input("Enter numbers: \n"))
    print('\x1bc')
    print("1.Addition\t2.Subtraction\n3.Multiplication\t4.Division\n5.Print last result\t6.Change Values")
    print("7.Print Values\t8.Exit")
    menu = input("Choose on of above option: ")
    if(menu == "1"):
        cal.add()
