from BO import Bo
from BLL import Bll


class View:
    def input(self):
        bo = Bo()
        print("Enter Number of watt:")
        bo._watt = float(input())
        print("Enter Number of unit:")
        bo._unit = float(input())

        Bll.write(self, bo)

    def show(self):
        bo = Bll.read(self)
        bo.display()
