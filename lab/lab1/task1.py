
name = input("Hello, what is your name?\n")
try:
    if(name.isdigit == True):
        raise TypeError("Value Not String")
except TypeError as te:
    print(te.__class__.__name__+" : "+te.__str__())
else:
    print("My name is Abubakar!\n")
