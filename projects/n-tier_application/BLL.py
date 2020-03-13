from DAL import Dal
from BO import Bo


class Bll:
    def read(self):
        return Dal.read(self)
        

    def write(self, bo):
        bo.calculate_bill()
        Dal.write(self,bo)
