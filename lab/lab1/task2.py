
try:
    class calculator():

        def __init__(self, value1=0, value2=0):
            self.__value1, self.__value2 = float(value1), float(value2)
            self.__result = 0

        def add(self):
            self.__result = self.__value1 + self.__value2

        def sub(self):
            self.__result = self.__value1 - self.__value2

        def mul(self):
            self.__result = self.__value1 * self.__value2

        def div(self):
            self.__result = self.__value1 / self.__value2

        def print(self):
            print("Your answer is "+self.__result.__str__())

    cal = calculator(input("Enter numbers: \n"),
                     input("Enter numbers: \n"))
    cal.add()

except ValueError as ve:
    print(ve.__class__.__name__ + " : Value not Numeric")
except ZeroDivisionError as zde:
    print(zde.__class__.__name__ + " : " + "Denominator is Zero ")


else:
    cal.print()
