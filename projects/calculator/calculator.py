
try:
    class calculator():

        def __init__(self, value1=0, value2=0):
            self.set_value1(value1)
            self.set_value2(value2)
            self.__result = 0

        def add(self):
            self.__result = self.__value1 + self.__value2
            self.print()

        def sub(self):
            self.__result = self.__value1 - self.__value2
            self.print()

        def mul(self):
            self.__result = self.__value1 * self.__value2
            self.print()

        def div(self):
            self.__result = self.__value1 / self.__value2
            self.print()

        def set_value1(self, value):
            self.__value1 = float(value)

        def set_value2(self, value):
            self.__value2 = float(value)

        def print(self):
            print("\nYour answer is "+self.__result.__str__())

        def print_value(self):
            print("\n1st Value = " + str(self.__value1) +
                  "\n2nd Value = " + str(self.__value2))

except ValueError as ve:
    print(ve.__class__.__name__ + " : Value not Numeric")
except ZeroDivisionError as zde:
    print(zde.__class__.__name__ + " : " + "Denominator is Zero ")
