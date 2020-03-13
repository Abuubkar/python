from BO import Bo

filein = "bill.in"


class Dal(object):
    def read(self):

        bo = Bo()
        with open("bill.in", mode='r') as file:
            bo._id, bo.watt, bo.unit, bo._bill = map(
                float, file.readline().split(','))
        return bo

    def write(self, bo):

        with open("bill.in", 'w') as file:
            file.write(
                ",".join([str(bo.id), str(bo.watt), str(bo.unit), str(bo.bill)]))
